"""Rebuild the portable artwork manifest and ZIP using the standard library."""
from pathlib import Path
import hashlib
import json
import re
import struct
import zipfile

ROOT = Path(__file__).resolve().parents[2]
BRAND = ROOT / 'brand'
KIT_VERSION = '2.2'
ARCHIVE = BRAND / 'downloads' / f'sovereign-ooda-brand-kit-v{KIT_VERSION}.zip'

def dimensions(path):
    data=path.read_bytes()
    if path.suffix.lower()=='.png':
        return struct.unpack('>II',data[16:24])
    if path.suffix.lower()=='.svg':
        match=re.search(r'<svg[^>]*width="(\d+)" height="(\d+)"',data.decode('utf-8'))
        return tuple(map(int,match.groups())) if match else None
    return None

files=[]
for path in BRAND.rglob('*'):
    relative=path.relative_to(BRAND)
    if not path.is_file() or any(p in {'downloads','history','node_modules','__pycache__','.git'} for p in relative.parts):
        continue
    if relative.as_posix()=='manifest.json':
        continue
    files.append(path)
files += [ROOT/'assets/sovereign-ooda-cover.jpg']
files += list((ROOT/'assets/roles').glob('*.png'))
files += [ROOT/'assets/roles/head-of-harness-engineering-odysseus.md']
files=sorted(set(files),key=lambda p:p.relative_to(ROOT).as_posix())
assets=[]
for path in files:
    data=path.read_bytes()
    record=dict(file=path.relative_to(ROOT).as_posix(),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    dims=dimensions(path)
    if dims:
        record.update(width=dims[0],height=dims[1])
    assets.append(record)
manifest=dict(brand='Sovereign OODA Harness',kit_version=KIT_VERSION,prepared_on='2026-11-20',
    status='Faceless Man Client Account Lead card and editable source added',
    asset_paths_relative_to='repository root',
    selection='Ben selected the mint/teal/orange character-card direction and requested the OODA kit and graphics be updated.',
    production='Image-tool artwork layers; native SVG type/geometry; bundled local OFL fonts; checked Chromium exports.',
    destination='https://sovereignharness.io/; displayed as sovereignharness.io on current shareable artwork',
    numbering='001 Baldwin, 002 Blake, 003 Harry; Research, Engineering and Client Account Lead unnumbered.',
    attribution='Ben O’Hanlon; retained film/photo credits on character cards. No invented photographer or quoted role copy.',
    archive=ARCHIVE.relative_to(ROOT).as_posix(),
    exclusions='Manifest and ZIP exclude their own checksums; historical files/downloads and development dependencies are outside the current archive.',
    assets=assets)
(BRAND/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
archive=ARCHIVE
archive.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as output:
    for path in files+[BRAND/'manifest.json']:
        output.write(path,path.relative_to(ROOT).as_posix())
with zipfile.ZipFile(archive) as check:
    assert check.testzip() is None
    for item in assets:
        assert hashlib.sha256(check.read(item['file'])).hexdigest()==item['sha256']
archive_checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
checksum_file = archive.with_name('SHA256SUMS.txt')
previous = checksum_file.read_text(encoding='utf-8').splitlines() if checksum_file.exists() else []
retained = [line for line in previous if not line.endswith('  ' + archive.name)]
checksum_file.write_text('\n'.join(retained + [f'{archive_checksum}  {archive.name}']) + '\n', encoding='utf-8', newline='\n')
print(json.dumps(dict(files=len(assets),archive_bytes=archive.stat().st_size,archive_sha256=archive_checksum,archive_verified=True)))
