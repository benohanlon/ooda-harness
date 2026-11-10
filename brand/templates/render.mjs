import { readFile, writeFile, mkdir, copyFile } from 'node:fs/promises';
import { dirname, resolve, extname } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const brand = resolve(here, '..');
const colors = JSON.parse(await readFile(resolve(brand,'tokens.json'),'utf8')).colors;
const { chromium } = await import(process.env.PLAYWRIGHT_MODULE || 'playwright');
const options = { headless: true };
if (process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE) options.executablePath = process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE;
const browser = await chromium.launch(options);
const page = await browser.newPage({ deviceScaleFactor: 1 });
const layouts = JSON.parse(await readFile(resolve(here, 'layouts.json'), 'utf8'));
const mime = { '.ttf':'font/ttf', '.woff2':'font/woff2', '.jpg':'image/jpeg', '.png':'image/png' };
const reports = [];

async function selfContained(source, path) {
  const files = new Set();
  for (const match of source.matchAll(/(?:href="|url\(')([^"')]+)(?:"|'\))/g)) {
    if (!match[1].startsWith('data:') && !match[1].startsWith('#')) files.add(match[1]);
  }
  for (const file of files) {
    if (/^[a-z]+:/i.test(file)) throw new Error('Only local dependencies are allowed: '+file);
    const bytes = await readFile(resolve(dirname(path),file));
    const uri = 'data:'+mime[extname(file)]+';base64,'+bytes.toString('base64');
    source = source.split(file).join(uri);
  }
  return source;
}

async function render(sourcePath, outputPath, requireCopy=false) {
  const original = await readFile(sourcePath,'utf8');
  const source = await selfContained(original,sourcePath);
  const dims = original.match(/<svg[^>]*width="(\d+)" height="(\d+)"/);
  if (!dims) throw new Error('Missing explicit dimensions: '+sourcePath);
  const width=Number(dims[1]),height=Number(dims[2]);
  await page.setViewportSize({width,height});
  await page.setContent('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;padding:0;background:#031C1D}svg{display:block}</style></head><body>'+source+'</body></html>');
  await page.evaluate(async()=>{
    await Promise.all([...document.fonts].map(font=>font.load()));
    await document.fonts.ready;
    await Promise.all([...document.querySelectorAll('image')].map(el=>new Promise((done,fail)=>{const img=new Image();img.onload=done;img.onerror=fail;img.src=el.getAttribute('href')})));
  });
  const inspection=await page.evaluate(({width,height,requireCopy})=>{
    const text=[...document.querySelectorAll('svg text')].map(el=>{const box=el.getBBox();return {text:el.textContent,slot:el.dataset.slot||null,weight:getComputedStyle(el).fontWeight,x:box.x,y:box.y,width:box.width,height:box.height}});
    const outside=text.filter(b=>b.x<0||b.y<0||b.x+b.width>width||b.y+b.height>height);
    const slotOverflow=text.filter(b=>b.slot==='name'&&b.x+b.width>482||b.slot==='role'&&b.x+b.width>1060||b.slot==='quote'&&b.x+b.width>1070||b.slot==='qualities'&&b.x<1080);
    const all=text.map(x=>x.text).join(' ');
    const copyOk=!requireCopy||["SOVEREIGN OODA HARNESS","THERE'S SOMETHING IN YOU THAT THE WORLD NEEDS","COUNTER-REVOLUTIONARY","MANOEUVRE WARFARE","COGNITIVE SUPERIORITY","WITHIN THE DISTRIBUTED MIND"].every(s=>all.includes(s));
    const destination=text.filter(t=>t.slot==='destination');
    const credit=text.find(t=>t.slot==='credit');
    const destinationOk=destination.length===1&&destination[0].text==='sovereignharness.io'&&(!credit||credit.x+credit.width+24<destination[0].x);
    return {outside,slotOverflow,copyOk,destinationOk,type:text.filter(t=>t.slot),fonts:[...document.fonts].map(f=>({family:f.family,weight:f.weight,status:f.status}))};
  },{width,height,requireCopy});
  if(inspection.outside.length||inspection.slotOverflow.length||!inspection.copyOk||!inspection.destinationOk||inspection.fonts.some(f=>f.status!=='loaded')) throw new Error(JSON.stringify({sourcePath,...inspection}));
  await mkdir(dirname(outputPath),{recursive:true});
  await page.locator('svg').screenshot({path:outputPath,animations:'disabled',...(extname(outputPath)==='.jpg'?{type:'jpeg',quality:92}:{})});
  reports.push({source:sourcePath.split(/[\\/]/).pop(),width,height,copy_checked:requireCopy,...inspection});
}

try {
  await mkdir(resolve(brand,'previews'),{recursive:true});
  for (const layout of layouts) await render(resolve(brand,layout.source),resolve(brand,layout.preview),layout.canonicalCopy!==false);
  await render(resolve(here,'cover-editable.svg'),resolve(brand,'assets/sovereign-ooda-cover-master.png'),true);
  await copyFile(resolve(brand,'previews/cover-editable.jpg'),resolve(brand,'../assets/sovereign-ooda-cover.jpg'));
  for (const name of ['colour-system','typography','profile-cards']) await render(resolve(brand,'previews',name+'.svg'),resolve(brand,'previews',name+'.png'));

  const items=[
    {id:'cover-editable',x:60,y:240,w:860,h:430,label:'FULL COVER / 1280 × 640',ly:718},
    {id:'compact-landscape',x:980,y:240,w:560,h:420,label:'COMPACT / 960 × 720',ly:718},
    {id:'square',x:60,y:818,w:600,h:600,label:'SQUARE / 1080 × 1080',ly:1470},
    {id:'portrait',x:790,y:818,w:480,h:600,label:'PORTRAIT / 1080 × 1350',ly:1470}
  ];
  const style = (await readFile(resolve(brand,'previews/colour-system.svg'),'utf8')).match(/<style>([\s\S]*?)<\/style>/)[1];
  const gallery=`<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1580" viewBox="0 0 1600 1580"><title>OODA editable layouts</title><style>${style}</style><rect width="1600" height="1580" fill="${colors.petrol_dark}"/><text class="mono" x="60" y="78" font-size="29" fill="${colors.mint}">SOVEREIGN OODA HARNESS</text><text class="mono" x="60" y="151" font-size="49" fill="${colors.mint}">EDITABLE LAYOUTS</text><text class="small" x="60" y="195" font-size="23" fill="${colors.signal_orange}">KIT 2.1 · SHARED COLOUR AND LIVE TYPE</text>${items.map(i=>`<rect x="${i.x-1}" y="${i.y-1}" width="${i.w+2}" height="${i.h+2}" fill="none" stroke="${colors.muted_teal}" stroke-opacity="0.5"/><image href="${i.id}.jpg" x="${i.x}" y="${i.y}" width="${i.w}" height="${i.h}"/><text class="small" x="${i.x}" y="${i.ly}" font-size="23" fill="${colors.mint}">${i.label}</text>`).join('')}<path d="M60 1510H1540" stroke="${colors.signal_orange}" stroke-width="2"/><text class="small" x="60" y="1552" font-size="22" fill="${colors.mint}">Same wording · Separate image and text · Bundled fonts</text></svg>`;
  const stampedGallery=gallery.replace('</svg>','<text class="mono" x="1540" y="1572" font-size="20" fill="'+colors.mint+'" text-anchor="end" data-slot="destination">sovereignharness.io</text></svg>');
  await writeFile(resolve(brand,'previews/layout-gallery.svg'),stampedGallery+'\n','utf8');
  await render(resolve(brand,'previews/layout-gallery.svg'),resolve(brand,'previews/layout-gallery.jpg'));
  if(process.env.OODA_RENDER_REPORT) await writeFile(process.env.OODA_RENDER_REPORT,JSON.stringify(reports,null,2)+'\n');
  console.log(JSON.stringify({rendered:reports.length,fontsLoaded:true,textWithinCanvas:true,canonicalCopyVerified:layouts.filter(l=>l.canonicalCopy!==false).length,profileCards:layouts.filter(l=>l.id.startsWith('profile-pack-')).length}));
} finally { await browser.close(); }
