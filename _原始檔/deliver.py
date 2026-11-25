"""把 sec/*.png 與 gif/enc 整理成交付資料夾（買三送一大禮包 v3 文青可愛風）。原始檔就放在交付資料夾的 _原始檔 裡，不另外複製。"""
import os, base64, io, shutil
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); O = os.path.dirname(D)
V = 'v3'; BASE = f'11.25_買三送一大禮包_落地頁_{V}'
SEC = [('s01', '01_封面_我的2027生活小夥伴', 0), ('s02', '02_認識四個生活小夥伴', 0), ('s03', '03_聖誕節前到貨_禮物緞帶_GIF', 1),
       ('s04', '04_跟著小夥伴過完一整天', 0), ('s05', '05_第1幕_早安小播報員_實體日曆_GIF', 1),
       ('s06', '06_第2幕_隨身小跟班_手機日曆_GIF', 1), ('s07', '07_第3幕_生活小祕書_手帳_GIF', 1),
       ('s08', '08_第4幕_暖心小信差_語錄卡_GIF', 1), ('s09', '09_幫小夥伴挑衣服_款式', 0),
       ('s10', '10_分給喜歡的人', 0), ('s11', '11_收尾_晚安明天見', 0)]
for sub in ['說明圖_1080寬', '動圖_MP4備用']:
    shutil.rmtree(f'{O}/{sub}', ignore_errors=True); os.makedirs(f'{O}/{sub}')
names = []
for sid, nm, g in SEC:
    if g:
        shutil.copy(f'{D}/gif/enc/{sid}.gif', f'{O}/說明圖_1080寬/{nm}.gif')
        shutil.copy(f'{D}/gif/enc/{sid}.mp4', f'{O}/動圖_MP4備用/{nm}.mp4')
        names.append((sid, nm + '.gif', g))
    else:
        Image.open(f'{D}/sec/{sid}.png').convert('RGB').save(f'{O}/說明圖_1080寬/{nm}.jpg', quality=90)
        names.append((sid, nm + '.jpg', g))
title = f'買三送一大禮包落地頁 {V} 文青可愛風'
head = f'<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>body{{margin:0;background:#888}}main{{max-width:432px;margin:0 auto;background:#FBF6EC}}img,video{{display:block;width:100%}}</style><main>'
dyn = head + '\n'.join(f'<img src="說明圖_1080寬/{n}">' for _, n, _ in names) + '</main>'
open(f'{O}/{BASE}_整頁預覽_動態.html', 'w').write(dyn)
open(f'{O}/index.html', 'w').write(dyn)
parts = []
for sid, n, g in names:
    if g:
        b = base64.b64encode(open(f'{D}/gif/enc/{sid}.mp4', 'rb').read()).decode()
        parts.append(f'<video autoplay muted loop playsinline src="data:video/mp4;base64,{b}"></video>')
    else:
        im = Image.open(f'{O}/說明圖_1080寬/{n}'); im = im.resize((864, round(im.height * 864 / im.width)), Image.LANCZOS)
        bio = io.BytesIO(); im.save(bio, 'JPEG', quality=86)
        parts.append(f'<img src="data:image/jpeg;base64,{base64.b64encode(bio.getvalue()).decode()}">')
open(f'{O}/{BASE}_整頁預覽_單檔整合.html', 'w').write(head + ''.join(parts) + '</main>')
ims = []
for sid, n, g in names:
    if g:
        SF = os.environ.get('SECFRAMES', f'{D}/gif/secframes')
        fs = sorted(os.listdir(f'{SF}/{sid}'))
        pick = {'s07': fs[-1], 's03': fs[0]}.get(sid, fs[len(fs) * 2 // 3])
        ims.append(Image.open(f'{SF}/{sid}/{pick}').convert('RGB'))
    else:
        ims.append(Image.open(f'{O}/說明圖_1080寬/{n}').convert('RGB'))
H = sum(i.height for i in ims); st = Image.new('RGB', (1080, H)); y = 0
for i in ims: st.paste(i, (0, y)); y += i.height
st = st.resize((540, H // 2), Image.LANCZOS)
st.save(f'{O}/{BASE}_整頁預覽_靜態第一格.jpg', quality=82)
for f in os.listdir(f'{O}/說明圖_1080寬'): print(f, os.path.getsize(f'{O}/說明圖_1080寬/{f}') // 1024, 'KB')
