"""買三送一大禮包（我全都要）落地頁 v3：文青可愛風「生活小夥伴繪日記」，2026-11-25。
阿寧看完電影版 v2：「再生成一個比較文青可愛風格的」。電影版 v2 保留，這支是另一款。

概念：四個產品＝四個生活小夥伴，陪你過完一天（沿用 v2 的「這四幕，是你一整天的分鏡」）。
  實體日曆＝早安小播報員、手機日曆＝隨身小跟班、手帳＝生活小祕書、語錄卡＝暖心小信差。
視覺：米白點點紙、棕色手繪小塗鴉（太陽、雲、紙飛機、咖啡杯、月亮、星星、愛心）、白邊商品貼紙、紙膠帶、
  粉彩色塊（奶油黃、天空藍、鼠尾草綠、薰衣草紫），照片是白邊相片＋紙膠帶。
字：中文全部凝書體（不加粗、不描邊），塗鴉是 SVG 不是字。頁寬 432，輸出 2.5 倍。
用法：python3 build_page.py → page.html"""
import os
D = os.path.dirname(os.path.abspath(__file__))
INK = '#4A3A30'
Y, B, G, L, P, R = '#F6DC8C', '#B9D3E6', '#BFD3B4', '#D5C6E3', '#F4C4B4', '#C9574B'

CSS = r"""
@font-face{font-family:CR;src:url(fonts_cream.otf)}
:root{--ink:#4A3A30;--soft:#8A7768;--paper:#FBF6EC;--card:#FFFDF8;--y:#F6DC8C;--b:#B9D3E6;--g:#BFD3B4;--l:#D5C6E3;--p:#F4C4B4;--r:#C9574B}
*{margin:0;padding:0;box-sizing:border-box}
body{width:432px;background:var(--paper);color:var(--ink);font-family:CR,serif;-webkit-font-smoothing:antialiased}
section{position:relative;overflow:hidden;background-color:var(--paper);background-image:radial-gradient(rgba(74,58,48,.14) 1px,transparent 1.4px);background-size:18px 18px;background-position:9px 9px}
.c{text-align:center}
.dd{position:absolute;overflow:visible}
.mk{background:linear-gradient(transparent 58%,var(--y) 58%,var(--y) 92%,transparent 92%);padding:0 2px}
.pill{display:inline-block;font-size:14px;letter-spacing:.14em;padding:6px 16px 6px 18px;border:1.5px dashed var(--ink);border-radius:30px;background:var(--card)}
.st{filter:drop-shadow(2.6px 0 0 #fff) drop-shadow(-2.6px 0 0 #fff) drop-shadow(0 2.6px 0 #fff) drop-shadow(0 -2.6px 0 #fff) drop-shadow(0 7px 9px rgba(74,58,48,.2))}
.tape{position:absolute;height:20px;opacity:.88;z-index:5;box-shadow:0 1px 2px rgba(74,58,48,.08)}
.t1{background:repeating-linear-gradient(45deg,rgba(255,255,255,.45) 0 4px,transparent 4px 8px),#F6DC8C}
.t2{background:radial-gradient(rgba(255,255,255,.75) 1.6px,transparent 2px) 0 0/8px 8px,#F4C4B4}
.t3{background:repeating-linear-gradient(90deg,rgba(255,255,255,.5) 0 3px,transparent 3px 9px),#BFD3B4}
.t4{background:repeating-linear-gradient(-45deg,rgba(255,255,255,.45) 0 4px,transparent 4px 8px),#B9D3E6}
.slip{position:absolute;z-index:6;background:var(--card);font-size:13px;letter-spacing:.08em;padding:5px 10px 5px 11px;border-radius:3px;box-shadow:0 3px 6px rgba(74,58,48,.16);white-space:nowrap}
h2{font-weight:normal;font-size:28px;line-height:1.45;letter-spacing:.08em}
.lead{font-size:14.5px;line-height:1.75;letter-spacing:.08em;color:var(--soft);margin-top:10px}

/* S01 封面 */
#s01{height:660px}
#s01 .pill{position:absolute;left:50%;top:38px;transform:translateX(-50%)}
#s01 h1{position:absolute;left:0;right:0;top:86px;font-weight:normal;font-size:42px;line-height:1.36;letter-spacing:.1em;padding-left:.1em}
#s01 .sub{position:absolute;left:0;right:0;top:214px;font-size:17px;letter-spacing:.14em}
#s01 .stk{position:absolute}
#s01 .tail{position:absolute;left:0;right:0;bottom:30px;font-size:14.5px;letter-spacing:.16em;color:var(--soft)}

/* S02 小夥伴介紹 */
#s02{padding:44px 20px 40px}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:24px}
.cd{background:var(--card);border-radius:16px;overflow:hidden;box-shadow:0 5px 14px rgba(74,58,48,.1);position:relative}
.cd .pn{height:150px;position:relative;overflow:hidden}
.cd .pn img{position:absolute;left:50%;transform:translateX(-50%)}
.cd .pn .stitch{position:absolute;left:10px;right:10px;bottom:0;border-top:1.5px dashed rgba(74,58,48,.45)}
.cd .tx{padding:12px 12px 14px;text-align:center}
.cd .tag{display:inline-block;font-size:11.5px;letter-spacing:.1em;padding:3px 10px;border-radius:20px;background:var(--paper);border:1px solid rgba(74,58,48,.25)}
.cd .nm{font-size:20px;letter-spacing:.06em;margin-top:8px}
.cd .ds{font-size:12.5px;line-height:1.65;letter-spacing:.04em;color:var(--soft);margin-top:6px}

/* S03 聖誕到貨 */
#s03{height:214px}
.gt{position:absolute;left:46px;right:46px;top:52px;height:118px;background:#B8473C;border-radius:18px;box-shadow:0 8px 16px rgba(120,40,30,.25)}
.gt .sw{position:absolute;inset:9px;border:2px dashed #E8C77E;border-radius:12px}
.gt .t{position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);text-align:center;font-size:34px;letter-spacing:.16em;padding-left:.16em;background:linear-gradient(180deg,#FCE9B0 0%,#EBC97E 50%,#CFA14F 100%);-webkit-background-clip:text;color:transparent}
.tw{animation:tw 2.5s ease-in-out infinite;transform-origin:center}
@keyframes tw{0%,100%{opacity:.25;transform:scale(.6)}25%{opacity:1;transform:scale(1.1)}50%{opacity:.4;transform:scale(.75)}}

/* S04 一日路線 */
#s04{padding:44px 0 30px}
.route{position:relative;height:610px;margin-top:10px}
.stop{position:absolute;width:432px}
.stop .ic{position:absolute;width:74px;height:74px;border-radius:50%;border:1.8px solid var(--ink);display:flex;align-items:center;justify-content:center;background:var(--card)}
.stop .tx{position:absolute;width:210px}
.stop .tm{font-size:22px;color:var(--r);letter-spacing:.04em}
.stop .tm span{font-size:15px;color:var(--ink);margin-left:8px;letter-spacing:.12em}
.stop .ac{font-size:15.5px;letter-spacing:.06em;margin-top:4px}
.stop .who{display:inline-block;font-size:12px;letter-spacing:.08em;padding:3px 10px;border-radius:20px;margin-top:7px}

/* 四幕 */
.scene{padding:40px 0 40px}
.scene .lab{display:flex;justify-content:center}
.scene .lab span{display:inline-flex;align-items:center;gap:8px;font-size:15px;letter-spacing:.12em;padding:6px 16px 6px 12px;border-radius:30px}
.scene h2{margin-top:14px}
.ph{position:relative;margin:24px auto 0;width:318px;background:#fff;padding:9px;border-radius:14px;box-shadow:0 8px 18px rgba(74,58,48,.16)}
.ph .v{width:300px;height:375px;border-radius:8px;background-size:cover;background-position:center}
.bub{position:relative;margin:26px 36px 0;background:var(--card);border:1.6px solid var(--ink);border-radius:18px;padding:12px 16px 13px;text-align:center}
.bub:before{content:"";position:absolute;left:50%;top:-10px;width:16px;height:16px;margin-left:-8px;background:var(--card);border-left:1.6px solid var(--ink);border-top:1.6px solid var(--ink);transform:rotate(45deg)}
.bub b{display:block;font-weight:normal;font-size:12.5px;letter-spacing:.12em;color:var(--soft)}
.bub p{font-size:17px;letter-spacing:.06em;margin-top:4px}
.ft{margin:20px 40px 0}
.ft div{display:flex;align-items:center;gap:10px;font-size:14.5px;letter-spacing:.05em;line-height:1.5;padding:5px 0}
.ft svg{flex:none}

/* S09 換裝 */
#s09{padding:44px 20px 40px}
.cs{position:relative;margin-top:20px;background:var(--card);border-radius:16px;padding:14px 14px 14px;box-shadow:0 5px 14px rgba(74,58,48,.08)}
.cs .h{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}
.cs .h b{font-weight:normal;font-size:17px;letter-spacing:.1em;padding:3px 12px;border-radius:20px}
.cs .h span{font-size:13px;color:var(--soft);letter-spacing:.08em}
.row5{display:flex;justify-content:space-between;align-items:flex-end;height:116px}
.row5 div{flex:1;text-align:center;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%}
.row5 img{max-width:62px;max-height:88px}
.row5 p{font-size:11.5px;letter-spacing:.04em;margin-top:7px;white-space:nowrap}
.phs{display:flex;gap:10px;align-items:flex-start}
.phs .pw{width:60px;height:94px;overflow:hidden;flex:none}
.phs .pw img{width:60px;display:block}
.chips{display:flex;flex-wrap:wrap;gap:6px;align-content:flex-start;padding-top:2px}
.chips span{font-size:12.5px;letter-spacing:.05em;border:1.3px solid rgba(74,58,48,.4);border-radius:20px;padding:4px 9px;background:var(--paper)}
.chips span.z{background:var(--l);border-color:transparent}
.ph5{height:130px;border-radius:10px;background-size:cover;background-position:center 58%}

/* S10 分享 */
#s10{padding:44px 0 42px}
#s10 .ph{width:378px;margin-top:22px}
#s10 .ph .v{width:360px;height:250px;background-position:center 8%}
.tags{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:26px 22px 0}
.tg{position:relative;background:var(--card);border-radius:10px 10px 10px 10px;padding:14px 12px 13px 26px;box-shadow:0 4px 10px rgba(74,58,48,.1)}
.tg:before{content:"";position:absolute;left:9px;top:50%;width:8px;height:8px;margin-top:-4px;border-radius:50%;border:1.5px solid var(--ink);background:var(--paper)}
.tg .p{font-size:12px;letter-spacing:.08em;color:var(--soft)}
.tg .to{font-size:15.5px;letter-spacing:.05em;margin-top:3px}
.tg .s{font-size:12px;letter-spacing:.03em;color:var(--soft);margin-top:4px;line-height:1.5}

/* S11 收尾 */
#s11{padding:40px 0 46px}
#s11 .ph{margin-top:0;transform:rotate(-1.2deg)}
#s11 h2{margin-top:30px}
#s11 .bye{margin-top:22px;font-size:30px;letter-spacing:.16em;padding-left:.16em}
#s11 .bye2{margin-top:8px;font-size:14.5px;letter-spacing:.14em;color:var(--soft)}
"""

# ---------- 手繪塗鴉（SVG，viewBox 48） ----------
def svg(body, size, style='', cls='dd'):
    return f'<svg class="{cls}" style="{style}" width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" stroke="{INK}" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'

def sun(size, style='', cls='dd'):
    rays = ''.join(f'<line x1="{24+13.5*c:.1f}" y1="{24+13.5*s:.1f}" x2="{24+(19 if i%2 else 17.5)*c:.1f}" y2="{24+(19 if i%2 else 17.5)*s:.1f}"/>'
                   for i, (c, s) in enumerate([(1, 0), (.71, .71), (0, 1), (-.71, .71), (-1, 0), (-.71, -.71), (0, -1), (.71, -.71)]))
    return svg(f'<circle cx="24" cy="24" r="9.5" fill="{Y}"/>{rays}<circle cx="20.6" cy="23" r="1" fill="{INK}" stroke="none"/><circle cx="27.4" cy="23" r="1" fill="{INK}" stroke="none"/><path d="M20.8 26.4 Q24 29.4 27.2 26.4"/>', size, style, cls)

def moon(size, style='', cls='dd'):
    return svg(f'<path d="M29 7 A17 17 0 1 0 41 33 A13.5 13.5 0 1 1 29 7 Z" fill="{Y}"/><path d="M17.5 27 q2 2 4 0"/><circle cx="16" cy="31.5" r="1.6" fill="{P}" stroke="none"/>', size, style, cls)

def cloud(size, style='', cls='dd'):
    return svg('<path d="M13 35 H36 a7 7 0 0 0 0.5 -14 a9.5 9.5 0 0 0 -17.5 -3.5 a7.5 7.5 0 0 0 -6 17.5 z" fill="#fff"/><circle cx="21" cy="28" r="0.9" fill="#4A3A30" stroke="none"/><circle cx="28" cy="28" r="0.9" fill="#4A3A30" stroke="none"/>', size, style, cls)

def plane(size, style='', cls='dd'):
    return svg(f'<path d="M6 24 L42 9 L31 40 L24 29 Z" fill="{B}"/><path d="M24 29 L42 9"/><path d="M4 33 q4 -2 7 1 q3 3 7 1" stroke-dasharray="2 3"/>', size, style, cls)

def cup(size, style='', cls='dd'):
    return svg(f'<path d="M11 21 H32 V30 a8.5 8.5 0 0 1 -8.5 8.5 h-4 a8.5 8.5 0 0 1 -8.5 -8.5 Z" fill="{P}"/><path d="M32 24 a4.5 4.5 0 0 1 0 9"/><path d="M18 8 q-2.5 3 0 6 q2.5 3 0 6"/><path d="M25 8 q-2.5 3 0 6 q2.5 3 0 6"/>', size, style, cls)

def spark(size, style='', color=Y, cls='dd'):
    return svg(f'<path d="M24 5 C25.6 18 30 22.4 43 24 C30 25.6 25.6 30 24 43 C22.4 30 18 25.6 5 24 C18 22.4 22.4 18 24 5 Z" fill="{color}" stroke-width="1.6"/>', size, style, cls)

def heart(size, style='', cls='dd'):
    return svg(f'<path d="M24 38 C10 29 7.5 19 14.5 13.5 C19.5 10 24 13.5 24 17 C24 13.5 28.5 10 33.5 13.5 C40.5 19 38 29 24 38 Z" fill="{P}"/>', size, style, cls)

def squig(w, style=''):
    return f'<svg class="dd" style="{style}" width="{w}" height="14" viewBox="0 0 {w} 14" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"><path d="M2 7 {" ".join(f"q{6} {-6 if i%2==0 else 6} 12 0" for i in range(int((w-4)/12)))}"/></svg>'


def tape(cls, style):
    return f'<i class="tape {cls}" style="{style}"></i>'


def scene(sid, no, label, icon, col, h2, lead, clip, who, says, feats, tapes, deco):
    f = ''.join(f'<div>{spark(16, "", col, "")}<span>{t}</span></div>' for t in feats)
    return f'''<section id="{sid}" class="scene">
<div class="lab"><span style="background:{col}">{icon}第 {no} 幕　{label}</span></div>
<h2 class="c">{h2}</h2>
<p class="lead c">{lead}</p>
<div class="ph">{tapes}<div class="v" data-clip="{clip}" style="background-image:url(gif/clips/{clip}/001.jpg)"></div></div>
{deco}
<div class="bub"><b>{who}說</b><p>{says}</p></div>
<div class="ft">{f}</div>
</section>'''


def build():
    s01 = f'''<section id="s01" class="c">
<span class="pill">煦暖曆全系列，一次到齊</span>
<h1>我的 2027<br><span class="mk">生活小夥伴</span></h1>
<p class="sub">這四幕，是你一整天的分鏡</p>
{sun(54, 'left:30px;top:84px;transform:rotate(-8deg)')}{spark(22, 'left:380px;top:96px')}{spark(14, 'left:362px;top:136px', P)}{cloud(50, 'left:350px;top:170px')}
<img class="stk st" src="img/h_cal.png" style="left:34px;top:280px;height:190px;transform:rotate(-7deg)">
{tape('t1', 'left:66px;top:268px;width:70px;transform:rotate(-14deg)')}
<span class="slip" style="left:28px;top:458px;transform:rotate(-5deg)">早安小播報員</span>
<img class="stk st" src="img/h_pl.png" style="left:158px;top:262px;height:236px;transform:rotate(3deg)">
{tape('t3', 'left:196px;top:252px;width:74px;transform:rotate(5deg)')}
<img class="stk st" src="img/h_qt.png" style="left:132px;top:440px;width:126px;transform:rotate(-4deg)">
<span class="slip" style="left:150px;top:560px;transform:rotate(2deg)">暖心小信差</span>
<div style="position:absolute;left:288px;top:286px;width:112px;height:230px;overflow:hidden;transform:rotate(6deg)"><img class="st" src="img/h_ph.png" style="position:absolute;left:5px;top:6px;width:102px"></div>
{tape('t4', 'left:316px;top:278px;width:62px;transform:rotate(12deg)')}
<span class="slip" style="left:282px;top:428px;transform:rotate(5deg);padding:8px 18px">隨身小跟班</span>
<span class="slip" style="left:206px;top:470px;transform:rotate(-3deg)">生活小祕書</span>
{heart(26, 'left:270px;top:574px;transform:rotate(12deg)')}{spark(18, 'left:110px;top:520px', B)}
<p class="tail">一份大禮包，陪你過好每一天</p>
</section>'''

    cards = [(Y, 'h_cal.png', 'height:126px;top:16px', '實體日曆', '早安小播報員', '每天早上，替你播報<br>今天的那一句話'),
             (B, 'h_ph.png', 'width:84px;top:22px', '手機日曆', '隨身小跟班', '走到哪跟到哪，<br>解鎖手機就見面'),
             (G, 'h_pl.png', 'height:128px;top:14px', '手帳', '生活小祕書', '幫你記行程，<br>也聽你說心事'),
             (L, 'h_qt.png', 'width:104px;top:30px', '語錄卡', '暖心小信差', '把說不出口的話，<br>替你送到對方手上')]
    cs = ''.join(f'<div class="cd"><div class="pn" style="background:{c}"><img class="st" src="img/{im}" style="{st}"><i class="stitch"></i></div><div class="tx"><span class="tag">{t}</span><p class="nm">{n}</p><p class="ds">{d}</p></div></div>' for c, im, st, t, n, d in cards)
    s02 = f'''<section id="s02">
<h2 class="c">認識一下，<br>你的四個生活小夥伴</h2>
{spark(20, 'left:52px;top:46px')}{heart(22, 'left:360px;top:86px;transform:rotate(10deg)')}
<div class="cards">{cs}</div>
</section>'''

    tws = ''.join(spark(sz, f'left:{x}px;top:{y}px;animation-delay:-{d}s', '#F3D58A', 'dd tw') for x, y, sz, d in [(30, 40, 24, 0), (384, 30, 20, .5), (20, 160, 18, 1.0), (392, 150, 26, 1.5), (210, 180, 14, 2.0)])
    s03 = f'''<section id="s03"><div class="gt"><i class="sw"></i><div class="t">聖誕節前到貨</div></div>
<svg class="dd" style="left:186px;top:24px" width="60" height="40" viewBox="0 0 60 40" fill="#E8C77E" stroke="#9C7A36" stroke-width="1.6" stroke-linejoin="round"><path d="M30 20 C20 6 6 6 8 16 C9 24 20 24 30 20 Z"/><path d="M30 20 C40 6 54 6 52 16 C51 24 40 24 30 20 Z"/><path d="M27 20 L20 36 L25 34 L27 38 L30 22 Z"/><path d="M33 20 L40 36 L35 34 L33 38 L30 22 Z"/><circle cx="30" cy="20" r="4.5"/></svg>
{tws}</section>'''

    stops = [(70, 'L', sun(52, '', ''), Y, '07:30', '早安', '撕下今天，讀一句話', '早安小播報員'),
             (210, 'R', plane(48, '', ''), B, '08:40', '出門', '解鎖手機，那句話還在', '隨身小跟班'),
             (350, 'L', cup(48, '', ''), G, '14:00', '午後', '攤開一週，排好生活', '生活小祕書'),
             (490, 'R', moon(46, '', ''), L, '22:30', '晚安', '抽一張卡，說聲晚安', '暖心小信差')]
    sp = ''
    for y, side, ic, col, tm, w, ac, who in stops:
        icx = 70 if side == 'L' else 288
        txx = 166 if side == 'L' else 52
        al = 'left' if side == 'L' else 'right'
        sp += f'<div class="stop" style="top:{y}px"><div class="ic" style="left:{icx}px;background:{col}">{ic}</div><div class="tx" style="left:{txx}px;top:2px;text-align:{al}"><p class="tm">{tm}<span>{w}</span></p><p class="ac">{ac}</p><span class="who" style="background:{col}">{who}</span></div></div>'
    path = f'<svg class="dd" style="left:0;top:0" width="432" height="610" viewBox="0 0 432 610" fill="none" stroke="{INK}" stroke-width="1.8" stroke-dasharray="3 7" stroke-linecap="round"><path d="M216 6 C216 40 140 40 107 70 M107 144 C110 200 300 170 325 210 M325 284 C320 330 120 310 107 350 M107 424 C110 470 300 450 325 490 M325 564 C325 590 216 590 216 606"/></svg>'
    s04 = f'''<section id="s04">
<h2 class="c">跟著小夥伴，<br>過完一整天</h2>
<div class="route">{path}{sp}{spark(18, 'left:207px;top:594px', P)}</div>
</section>'''

    def ph_tapes(a, b):
        return tape(a, 'left:-14px;top:12px;width:70px;transform:rotate(-38deg)') + tape(b, 'right:-14px;top:12px;width:70px;transform:rotate(38deg)')

    s05 = scene('s05', 1, '早上 07:30', sun(24, '', ''), Y, '撕下昨天，<br>把今天的第一句話收下', '起床第一眼，先看見一句溫柔的話，<br>今天就有了好的開始。', 'x_tear',
                '早安小播報員', '早安！今天這一句，是寫給你的。', ['一天一頁，陪你 365 天', '五款任選：煦暖曆、幹話曆、鮮花圖鑑、<br>旅行機票、日日法華'],
                ph_tapes('t1', 't2'), spark(22, 'left:28px;top:300px') + spark(14, 'left:392px;top:520px', P))
    s06 = scene('s06', 2, '出門 08:40', plane(24, '', ''), B, '出了門，<br>今天那句話也跟著你', '上班、出差、午休，<br>解鎖手機就看得到，不怕忘記撕。', 'c_where',
                '隨身小跟班', '你去哪裡，我就跟到哪裡。', ['桌面小工具，三種尺寸任你放', '十六款任選，iOS、Android 都能用'],
                ph_tapes('t4', 't1'), cloud(44, 'left:14px;top:280px') + spark(16, 'left:394px;top:300px', B))
    s07 = scene('s07', 3, '午後 14:00', cup(24, '', ''), G, '找一間咖啡廳，<br>把生活排進一頁裡', '開會、待辦、想做的小事，<br>寫下來，心就安定了。', 'p_week',
                '生活小祕書', '行程交給我，心事也可以喔。', ['週計畫、月計畫、年計畫，一本排好', '12 個自我覺察主題，寫給自己看'],
                ph_tapes('t3', 't2'), heart(22, 'left:22px;top:300px;transform:rotate(-10deg)') + spark(16, 'left:394px;top:540px', G))
    s08 = scene('s08', 4, '睡前 22:30', moon(24, '', ''), L, '抽一張卡，<br>跟今天的自己說晚安', '累了就抽一張給自己，<br>想念誰，也可以抽一張送他。', 'q_draw',
                '暖心小信差', '說不出口的話，我幫你送過去。', ['45 張中英雙語語錄卡', '手機碰一下收藏盒，看每張卡的延伸解讀'],
                ph_tapes('t2', 't4'), spark(20, 'left:24px;top:296px', L) + spark(14, 'left:396px;top:300px'))

    cal = ''.join(f'<div><img class="st" src="img/{f}.png" style="{"max-width:78px" if f == "c_tr" else ""}"><p>{n}</p></div>' for f, n in [('c_xn', '煦暖曆'), ('c_gh', '幹話曆'), ('c_fl', '鮮花圖鑑'), ('c_tr', '旅行機票'), ('c_fh', '日日法華')])
    pls = ''.join(f'<div><img class="st" src="img/{f}.png" style="max-height:92px"><p>{n}</p></div>' for f, n in [('pl_d', '晨曦米白'), ('pl_a', '沙丘暖杏'), ('pl_b', '靜海霧藍'), ('pl_c', '森語墨綠')])
    s09 = f'''<section id="s09">
<h2 class="c">幫小夥伴們，<br>挑一件喜歡的衣服</h2>
<p class="lead c">每一位都能選款式，挑成你最喜歡的樣子</p>
{spark(20, 'left:40px;top:50px', B)}{spark(16, 'left:378px;top:58px', P)}
<div class="cs">{tape('t1', 'left:150px;top:-9px;width:60px;transform:rotate(-4deg)')}<div class="h"><b style="background:{Y}">早安小播報員</b><span>實體日曆，五款選一</span></div><div class="row5">{cal}</div></div>
<div class="cs"><div class="h"><b style="background:{B}">隨身小跟班</b><span>手機日曆，十六款選一</span></div>
<div class="phs"><div class="pw"><img src="img/ph_xn.png"></div><div class="pw"><img src="img/ph_gh.png"></div><div class="pw"><img src="img/ph_tr.png"></div>
<div class="chips"><span>煦暖曆</span><span>旅行曆</span><span>鮮花圖鑑</span><span>幹話曆</span><span class="z">12 星座曆</span></div></div></div>
<div class="cs"><div class="h"><b style="background:{G}">生活小祕書</b><span>手帳，開窗款、素面款各四色</span></div><div class="row5" style="height:108px">{pls}</div></div>
<div class="cs"><div class="h"><b style="background:{L}">暖心小信差</b><span>語錄卡，五色收藏盒</span></div><div class="ph5" style="background-image:url(img/qt5.jpg)"></div></div>
</section>'''

    gifts = [('早安小播報員', '送天天見面的同事', '每撕一頁，就想起你一次'),
             ('隨身小跟班', '送住在遠方的朋友', '轉寄一封兌換碼，<br>人在國外也收得到'),
             ('暖心小信差', '送最懂你的好朋友', '那句說不出口的話，<br>讓卡片替你說'),
             ('生活小祕書', '留給自己', '2027，記得好好<br>照顧自己')]
    tg = ''.join(f'<div class="tg"><p class="p">{a}</p><p class="to">{b}</p><p class="s">{c}</p></div>' for a, b, c in gifts)
    s10 = f'''<section id="s10">
<h2 class="c">也可以把小夥伴，<br>分給喜歡的人</h2>
<p class="lead c">一份大禮包，拆開就是四份心意</p>
<div class="ph">{tape('t2', 'left:-12px;top:10px;width:66px;transform:rotate(-36deg)')}{tape('t3', 'right:-12px;top:10px;width:66px;transform:rotate(36deg)')}<div class="v" style="background-image:url(img/gift.jpg)"></div></div>
{heart(24, 'left:24px;top:150px;transform:rotate(-12deg)')}{spark(18, 'left:392px;top:150px', P)}
<div class="tags">{tg}</div>
</section>'''

    s11 = f'''<section id="s11">
<div class="ph">{tape('t1', 'left:-12px;top:12px;width:70px;transform:rotate(-36deg)')}{tape('t4', 'right:-12px;top:12px;width:70px;transform:rotate(36deg)')}<div class="v" style="background-image:url(img/end.jpg)"></div></div>
{spark(24, 'left:30px;top:60px')}{heart(22, 'left:384px;top:330px;transform:rotate(14deg)')}
<h2 class="c">你負責好好生活，<br>其他的，交給小夥伴們。</h2>
<p class="bye c">{moon(34, 'vertical-align:-6px;margin-right:10px', '')}晚安，明天見。{spark(18, 'vertical-align:4px;margin-left:4px', Y, '')}</p>
<p class="bye2 c">2027 的每一天，它們都在</p>
</section>'''

    html = f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{s01}{s02}{s03}{s04}{s05}{s06}{s07}{s08}{s09}{s10}{s11}</body></html>'
    open(f'{D}/page.html', 'w').write(html)
    print('page.html', len(html))


if __name__ == '__main__':
    build()
