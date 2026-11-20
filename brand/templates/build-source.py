"""Build editable OODA artwork sources from shared tokens and card content.

Uses the standard library only. Photographic layers are generated separately;
this script typesets native SVG and never edits their raster pixels.
"""
from pathlib import Path
import json
import html

BRAND = Path(__file__).resolve().parent.parent
ROOT = BRAND.parent
T = json.loads((BRAND / 'tokens.json').read_text(encoding='utf-8'))
C = T['colors']
BG, MINT, MUTED, ORANGE = (C[k] for k in ('petrol_dark', 'mint', 'muted_teal', 'signal_orange'))

STYLE = """
@font-face{font-family:OodaMono;src:url('../fonts/IBMPlexMono-Regular.ttf');font-weight:400}
@font-face{font-family:OodaMono;src:url('../fonts/IBMPlexMono-Medium.ttf');font-weight:500}
@font-face{font-family:OodaSans;src:url('../fonts/Inter-Bold.woff2');font-weight:700}
@font-face{font-family:OodaCondensed;src:url('../fonts/BarlowCondensed-Regular.ttf');font-weight:400}
@font-face{font-family:OodaCondensed;src:url('../fonts/BarlowCondensed-Bold.ttf');font-weight:700}
@font-face{font-family:OodaCondensed;src:url('../fonts/BarlowCondensed-Black.ttf');font-weight:900}
text{font-kerning:normal;text-rendering:geometricPrecision}
.mono,.small{font-family:OodaMono,monospace;font-weight:400}
.mono{font-weight:500}.message,.sans{font-family:OodaSans,sans-serif;font-weight:700}
.condensed{font-family:OodaCondensed,sans-serif;font-weight:700}
"""

def text(x, y, value, size=28, color=MINT, cls='sans', anchor='start', weight=None, extra=''):
    w = f' font-weight="{weight}"' if weight else ''
    if weight:
        w += f' style="font-weight:{weight}"'
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" class="{cls}" text-anchor="{anchor}"{w} {extra}>{html.escape(value)}</text>'

def line(x1, y1, x2, y2, color=MINT, width=2, extra=''):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}" {extra}/>'

def url_footer(w, h, size=20, inset=32, baseline=None):
    return text(w-inset, h-14 if baseline is None else baseline, T['destination']['display'], size, cls='mono', anchor='end', extra='data-slot="destination"')

def svg(w, h, title, body):
    if 'data-slot="destination"' not in body:
        body += url_footer(w, h)
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{html.escape(title)}</title><style>{STYLE}</style><rect width="{w}" height="{h}" fill="{BG}"/>{body}</svg>\n'

def write(path, content):
    dest = BRAND / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding='utf-8', newline='\n')

def research_loop():
    """Draw a compact version of Boyd's OODA relationships over the woodland."""
    white = '#FFFFFF'
    diagram = """
<defs>
  <radialGradient id="research-loop-shade">
    <stop offset="0.55" stop-color="#031C1D" stop-opacity="0.8"/>
    <stop offset="0.8" stop-color="#031C1D" stop-opacity="0.58"/>
    <stop offset="1" stop-color="#031C1D" stop-opacity="0"/>
  </radialGradient>
  <marker id="research-loop-arrow" markerWidth="4" markerHeight="4" refX="3.5" refY="2" orient="auto" viewBox="0 0 4 4">
    <path d="M0 0L4 2L0 4Z" fill="#FFFFFF"/>
  </marker>
</defs>
<g aria-label="OODA loop with implicit guidance and feedback">
  <rect x="100" y="159" width="1336" height="546" fill="url(#research-loop-shade)"/>
  <g fill="none" stroke="#FFFFFF" stroke-linecap="round" stroke-linejoin="round">
    <g stroke-width="5" marker-end="url(#research-loop-arrow)">
      <path d="M465 426H536"/>
      <path d="M756 426H831"/>
      <path d="M1034 426H1109"/>
    </g>
    <g stroke-width="3.5" opacity="0.82" marker-end="url(#research-loop-arrow)">
      <path d="M595 335V276H350V368"/>
      <path d="M698 335V276H1211V368"/>
      <path d="M1211 479V576H350V484"/>
    </g>
    <g stroke-width="5" fill="#031C1D" fill-opacity="0.68">
      <ellipse cx="350" cy="426" rx="115" ry="52"/>
      <circle cx="647" cy="426" r="108"/>
      <path d="M871 374H995L1034 426L995 478H871L832 426Z"/>
      <rect x="1112" y="374" width="198" height="104"/>
    </g>
    <path d="M933 479V576" stroke-width="3.5" opacity="0.82"/>
  </g>"""
    for x, label in ((350, 'OBSERVE'), (647, 'ORIENT'), (933, 'DECIDE'), (1211, 'ACT')):
        diagram += text(x, 444, label, 58 if label == 'ORIENT' else 49, white, 'condensed', 'middle')
    diagram += text(954, 257, 'IMPLICIT GUIDANCE', 28, white, 'mono', 'middle')
    diagram += text(782, 614, 'FEEDBACK', 28, white, 'mono', 'middle')
    return diagram + '</g>'

cards = json.loads((BRAND / 'profile-cards.json').read_text(encoding='utf-8'))
layouts = []
for card in cards:
    geometry = T['profile_card']
    w, h = geometry['width'], geometry['height']
    image = card['image']
    if card.get('source_card'):
        picture = f'<image href="../assets/character-sources/{image}" x="0" y="0" width="1536" height="1024" clip-path="url(#picture)"/>'
    else:
        picture = f'<image href="../assets/character-sources/{image}" x="24" y="60" width="1488" height="744" preserveAspectRatio="xMidYMid slice" clip-path="url(#picture)"/>'
    body = '<defs><clipPath id="picture"><rect x="24" y="60" width="1488" height="744"/></clipPath></defs>' + picture
    if card['id'] == 'research':
        body += research_loop()
    if card['id'] == '001':
        quote_lines = [
            ('A King may move a man,', 133, 400),
            ('a father may claim a son, but remember that', 167, 400),
            ('even when those who move you be Kings, or men of power,', 201, 400),
            ('your soul is in your keeping alone.', 270, 700),
            ('When you stand before God, you cannot say,', 336, 400),
            ('“But I was told by others to do thus.”', 383, 400),
            ('Or that, “Virtue was not convenient at the time.”', 430, 400),
            ('This will not suffice.', 520, 400),
            ('Remember that.', 556, 400),
        ]
        for value, y, weight in quote_lines:
            body += text(62, y, value, 30, cls='condensed', weight=weight)
    # All labels below are live type. The exact same positions and sizes serve every card.
    body += f'<rect x="12" y="12" width="1512" height="1000" fill="none" stroke="{MINT}" stroke-width="2"/>'
    body += line(40, 25, 40, 46, ORANGE, 4)
    body += text(61, 45, 'HERMES', 26, cls='mono', extra='letter-spacing="5"')
    header = 'OODA HARNESS / PROFILE PACK ' + card['id'] if card['id'].isdigit() else 'OODA HARNESS / ' + ' '.join(card['role_lines'])
    body += text(1501, 42, header, 18, cls='small', anchor='end', extra='letter-spacing="1.7"')
    body += line(26, 58, 1510, 58) + line(26, 804, 1510, 804) + line(26, 970, 1510, 970)
    body += line(geometry['divider_x'], 820, geometry['divider_x'], 954, ORANGE, 3)
    if card.get('name_lines'):
        for index, name in enumerate(card['name_lines']):
            body += text(38, 886 + index * 73, name, 94, cls='condensed', weight=900, extra='data-slot="name"')
    else:
        body += text(38, 932, card['name'], geometry['name_font_size'], cls='condensed', weight=900, extra='data-slot="name"')
    if card.get('surname'):
        body += text(41, 959, card['surname'], 26, cls='condensed', weight=700, extra='letter-spacing="2"')
    for i, value in enumerate(card['role_lines']):
        body += text(geometry['title_x'], 851 + i*41, value, geometry['title_font_size'], cls='condensed', extra='letter-spacing="1.5" data-slot="role"')
    for i, value in enumerate(card['quote_lines']):
        weight = 400 if card['id'] == '003' and i == 0 else 700
        body += text(geometry['title_x'], 926 + i*geometry['quote_line_height'], value, geometry['quote_font_size'], ORANGE, 'condensed', weight=weight, extra='data-slot="quote"')
    for i, value in enumerate(card['qualities']):
        body += text(1500, 869 + i*31, value, 16, cls='small', anchor='end', extra='letter-spacing="1.6" data-slot="qualities"')
    body += text(39, 995, card['credit'], 14, cls='small', extra='data-slot="credit"')
    body += url_footer(w, h, 22, 37, 998)
    source = 'templates/profile-pack-' + card['id'] + '.svg'
    label = 'Profile Pack ' + card['id'] if card['id'].isdigit() else 'role card'
    write(source, svg(w, h, card['name'] + ' / ' + ' '.join(card['role_lines']) + ' / ' + label, body))
    layouts.append(dict(id='profile-pack-' + card['id'], width=w, height=h, source=source, preview=card['output'], canonicalCopy=False, status='new-style artwork'))

# Existing cover layouts retain their composition and exact copy; recolour only their native layers.
old_colors = {'#07140F': BG, '#20784E': MUTED, '#A2BA91': MUTED, '#C6A45D': ORANGE, '#F1EBD7': MINT, '#C9C5B5': MINT}
for name in ('cover-editable', 'compact-landscape', 'square', 'portrait'):
    p = BRAND / 'templates' / (name + '.svg')
    s = p.read_text(encoding='utf-8')
    for before, after in old_colors.items():
        s = s.replace(before, after)
    s = s.replace('../assets/eye-clean-prototype.jpg', '../assets/eye-mint-source.png')
    s = s.replace('prototype', 'layout').replace('Prototype', 'Editable')
    import re
    m = re.search(r'<svg[^>]*width="(\d+)" height="(\d+)"', s)
    # Add a reproducible destination line without moving the accepted cover copy.
    s = re.sub(r'<text[^>]*data-slot="destination"[^>]*>.*?</text>', '', s)
    s = s.replace('No embedded attribution.', 'Visible destination URL; creator attribution in metadata.')
    width, height = int(m[1]), int(m[2])
    s = s.replace('</svg>', url_footer(width, height, 18 if height < 800 else 22, 42) + '</svg>')
    p.write_text(s, encoding='utf-8', newline='\n')
    layouts.insert(0, dict(id=name,width=int(m[1]),height=int(m[2]),source='templates/'+name+'.svg',preview='previews/'+name+'.jpg',canonicalCopy=True,status='new-style editable layout'))

def box(x,y,w,h,lines,accent=False):
    b=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{BG}" stroke="{ORANGE if accent else MUTED}" stroke-width="2"/>'
    for i,value in enumerate(lines):
        b+=text(x+w/2,y+34+i*29,value,25 if i==0 else 20,cls='sans' if i==0 else 'small',anchor='middle')
    return b

arrow_defs=f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="{ORANGE}"/></marker></defs>'
def arrow(points):
    return f'<path d="{points}" fill="none" stroke="{ORANGE}" stroke-width="3" marker-end="url(#arrow)"/>'

# Redraw the illustrative diagrams as native vectors; meaning follows current Ecology of Mind.
b=arrow_defs+text(45,48,'SOVEREIGN OODA HARNESS',21,cls='mono')+line(45,66,1209,66)
b+=text(45,135,'The cognitive dipole',65)+text(45,182,'One role. Two agents. A shared purpose.',32)
b+=text(45,224,'PAIRED MODE / SELECTIVELY COMMISSIONED',19,ORANGE,'mono')
b+=f'<rect x="35" y="270" width="1090" height="550" rx="45" fill="none" stroke="{MUTED}" stroke-width="2"/>'
for cx, cy, r in [(225,500,155),(600,500,175),(960,500,155)]:
    b+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BG}" stroke="{MINT}" stroke-width="3"/>'
for x, values in [(225,['Agent A','Doer / builder / giver','Complete OODA','Observe · Orient','Decide · Act']),(960,['Agent B','Observer / active receiver','Complete OODA','Observe · Orient','Decide · Act'])]:
    for i,value in enumerate(values):
        b+=text(x,451+i*36,value,34 if i==0 else 18,cls='sans' if i==0 else 'small',anchor='middle')
for i,value in enumerate(['Shared nucleus','Role purpose & contract','Combined shared/private basis','System-wide units of account','Numbers before strategy']):
    b+=text(600,440+i*34,value,32 if i==0 else 18,cls='sans' if i==0 else 'small',anchor='middle')
b+=arrow('M300 350Q600 280 889 350')+arrow('M885 678Q600 720 310 677')
b+=text(600,294,'Evidence · challenge · correction',22,cls='small',anchor='middle')
b+=text(600,749,'Complementary, reversible polarities',26,ORANGE,anchor='middle')
b+=text(600,787,'One owner per shared action.',22,cls='small',anchor='middle')
b+=text(600,874,'Bounded contributions',28,anchor='middle')
for x, value in [(65,'Find prior work'),(425,'Check a source'),(785,'Test a claim')]:
    b+=box(x,908,305,68,[value])
b+=arrow('M225 815L225 900')+arrow('M960 900L960 820')
b+=text(600,1019,'Temporary contributors return evidence.',21,cls='small',anchor='middle')
b+=box(375,1085,450,65,['World & other people'],True)
b+=arrow('M1125 545L1200 545L1200 1117L830 1117').replace('marker-end=', 'marker-start="url(#arrow)" marker-end=')
b+=text(1190,982,'Action / response',19,cls='small',anchor='end')
b+=line(45,1182,1209,1182)
b+=text(45,1215,'Ordinary work can use one accountable agent. Illustration, not runtime evidence.',17,cls='small')
write('templates/cognitive-dipole.svg',svg(1254,1254,'Cognitive dipole: selectively commissioned paired mode',b))
layouts.append(dict(id='cognitive-dipole',width=1254,height=1254,source='templates/cognitive-dipole.svg',preview='assets/cognitive-dipole-v1.png',canonicalCopy=False,status='illustrative paired mode'))

b=arrow_defs+text(40,52,'SOVEREIGN OODA HARNESS',31,cls='mono')+text(40,96,'From human purpose to bounded work',27)
b+=line(40,122,984,122)
b+=box(130,158,710,85,['The sovereign','Human purpose, judgement and authority'],True)
b+=box(130,290,710,85,['The ecology','Roles · projects · people · knowledge'])
b+=arrow('M130 199L70 199L70 333L125 333')
b+=text(64,270,'Direction',19,ORANGE,'mono')
b+=arrow('M840 332L944 332L944 200L845 200')
b+=text(973,273,'Feedback',18,ORANGE,'mono','end')
b+=f'<rect x="55" y="427" width="735" height="530" rx="12" fill="none" stroke="{MINT}" stroke-width="3"/>'
b+=text(85,475,'One enduring role',35)+text(85,515,'One accountable agent for ordinary work.',21,cls='small')
b+=text(85,553,'Selective paired mode for evaluation / high-value work',19,ORANGE,'mono')
b+=box(90,579,665,106,['Combined governing basis','Shared role + private application','Purpose · contract · system-wide units of account'])
b+=box(90,725,310,156,['Agent A / doer','Complete OODA','Observe · Orient','Decide · Act'])
b+=box(445,725,310,156,['Agent B / receiver','Complete OODA','Observe · Orient','Decide · Act'])
b+=arrow('M405 768L440 768')+arrow('M440 835L405 835')
b+=text(422,924,'Evidence · challenge · correction · reversible positions',18,cls='small',anchor='middle')
b+=box(812,589,192,105,['World &','other people'],True)
b+=arrow('M790 620L806 620')+arrow('M812 676L797 676')
b+=text(906,735,'Action / response',16,ORANGE,'small',anchor='middle')
b+=box(55,1010,915,110,['Maintained context','Guidance · private profile · prior learning','Retrieve / retain with the existing owner'])
b+=arrow('M420 957L420 1003').replace('marker-end=', 'marker-start="url(#arrow)" marker-end=')
b+=box(55,1175,915,132,['Bounded contributions','Temporary workers · skills · tools · records','Useful work and evidence return to the accountable role'])
b+=arrow('M55 925L25 925L25 1230L50 1230').replace('marker-end=', 'marker-start="url(#arrow)" marker-end=')
b+=box(55,1364,915,86,['Enabling infrastructure','Models · runtimes · connectors · storage · compute'])
b+=line(40,1485,984,1485)+text(40,1517,'Illustration in development. Written contracts govern interpretation.',16,cls='small')
write('templates/ecology-stack.svg',svg(1024,1536,'OODA ecology: direct work and selective paired operation',b))
layouts.append(dict(id='ecology-stack',width=1024,height=1536,source='templates/ecology-stack.svg',preview='assets/sovereign-ooda-ecology-stack.png',canonicalCopy=False,status='illustrative overview'))

# Shared specimens use actual bundled fonts and the same semantic palette.
b=text(48,70,'OODA / COLOUR SYSTEM',30,cls='mono')
for i,(label,color) in enumerate(C.items()):
    x=48+i*296
    b+=f'<rect x="{x}" y="125" width="260" height="200" fill="{color}" stroke="{MINT}"/>'
    b+=text(x,370,label.replace('_',' ').upper(),21,cls='mono')+text(x,410,color,25,cls='mono')
b+=text(48,480,'Flat ink colours for live type and diagrams; artwork retains its tonal range.',20,cls='small')
write('previews/colour-system.svg',svg(1280,530,'OODA shared colour system',b))
b=text(50,70,'OODA / TYPE SYSTEM',30,cls='mono')
b+=text(50,210,'BALDWIN · BLAKE · HARRY',102,cls='condensed',weight=900)
b+=text(50,285,'BARLOW CONDENSED / NAMES AND ROLE TITLES',22,ORANGE,'mono')
b+=text(50,365,'Right now I’m in first gear.',45,ORANGE,'condensed',weight=400)
b+=text(50,423,'Would you like to see me shift to six?',45,ORANGE,'condensed',weight=700)
b+=text(50,495,'ONE FAMILY / SAME SIZE / DELIBERATE WEIGHT CONTRAST',19,cls='mono')
b+=text(50,580,'IBM Plex Mono / headers, pack IDs, metadata',25,cls='mono')
b+=text(50,655,'Inter Bold / messages and diagram hierarchy',30)
write('previews/typography.svg',svg(1440,720,'OODA shared live typography',b))

b=text(50,65,'OODA / CHARACTER COLLECTION',32,cls='mono')
b+=text(50,112,'One palette, one type system, fixed columns. Research/Engineering pack numbers remain unassigned.',18,cls='small')
for i,card in enumerate(cards):
    col,row=i%2,i//2
    x,y=50+col*1160,155+row*825
    href='../'+card['output']
    b+=f'<image href="{href}" x="{x}" y="{y}" width="1100" height="733.333"/>'
    b+=text(x,y+775,card['name']+' / '+' '.join(card['role_lines']),21,cls='mono')
write('previews/profile-cards.svg',svg(2370,2630,'OODA coherent character-card collection',b))
(BRAND/'templates/layouts.json').write_text(json.dumps(layouts,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'editable_layouts':len(layouts),'profile_cards':len(cards),'colors':C}))
