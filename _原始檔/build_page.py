"""買三送一大禮包（我全都要）落地頁 v1，2026-11-25。
阿寧：「還要買三送一大禮包，另外設計一個落地頁。他等於煦暖曆所有商品都買了，這要是完全不同的設計風格，
要給他『買這四個產品』可以在他生活扮演什麼角色。」

隱喻：一部叫《好好生活》的電影。你是主角，四個產品是配角，各自「飾」一個生活角色。
視覺：暖黑片場底、膠卷齒孔框、場記板、演員表、通告單、戲院跑馬燈（跟單品頁的米白紙感完全不同）。
字：中文凝書體（不加粗、不描邊），英文小標 Helvetica 寬字距。頁寬 432，輸出 2.5 倍。
用法：python3 build_page.py → page.html"""
import os, math
D = os.path.dirname(os.path.abspath(__file__))

CSS = r"""
@font-face{font-family:CR;src:url(fonts_cream.otf)}
:root{--ink:#17120E;--ink2:#211A15;--ink3:#2C231D;--cream:#F3E9D9;--mute:#B3A48E;--amber:#E0A65C;--red:#BC443C;--paper:#F2E8D7;--pink:#3A2A20}
*{margin:0;padding:0;box-sizing:border-box}
body{width:432px;background:var(--ink);color:var(--cream);font-family:CR,serif;-webkit-font-smoothing:antialiased}
section{position:relative;overflow:hidden;background:var(--ink)}
.en{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;letter-spacing:.3em;font-size:9.5px;text-transform:uppercase}
.amber{color:var(--amber)} .mute{color:var(--mute)} .c{text-align:center}
.hl{color:var(--amber)}

/* 膠卷 */
.strip{background:#0B0807;padding:16px 12px;position:relative}
.strip .holes{position:absolute;left:0;right:0;height:7px;background-image:linear-gradient(90deg,rgba(243,233,217,.5) 0 9px,transparent 9px 18px);background-size:18px 7px;background-position:5px 0}
.strip .holes.t{top:4.5px} .strip .holes.b{bottom:4.5px}
.strip .edge{position:absolute;font-family:"Helvetica Neue",Helvetica,sans-serif;font-size:6.5px;letter-spacing:.22em;color:var(--amber);opacity:.85}
.frames{display:flex;gap:8px}
.frames div{flex:1;aspect-ratio:4/5;background-size:cover;background-position:center;border-radius:2px}

/* S01 片頭 */
#s01{padding:44px 0 34px}
#s01 .pre{margin-bottom:22px}
#s01 .kick{font-size:17px;letter-spacing:.2em;color:var(--mute);margin-bottom:12px}
#s01 h1{font-weight:normal;font-size:50px;line-height:1.28;letter-spacing:.06em}
#s01 .sub{font-size:19px;letter-spacing:.12em;margin:16px 0 30px;color:var(--cream)}
#s01 .sub .hl{border-bottom:1.5px solid var(--amber);padding-bottom:2px}
#s01 .names{display:flex;gap:8px;padding:12px 12px 0}
#s01 .names div{flex:1;text-align:center}
#s01 .names .en{display:block;font-size:8.5px;letter-spacing:.25em;margin-bottom:5px}
#s01 .names b{font-weight:normal;font-size:15.5px;letter-spacing:.08em}
#s01 .tail{margin-top:28px;font-size:14px;letter-spacing:.2em;color:var(--mute)}

/* S02 演員表 */
#s02{padding:44px 26px 40px}
#s02 h2{font-weight:normal;font-size:34px;letter-spacing:.3em;margin:8px 0 26px;padding-left:.3em}
.star{display:flex;align-items:baseline;justify-content:center;gap:16px;padding:16px 0 18px;border-top:1px solid rgba(243,233,217,.22);border-bottom:1px solid rgba(243,233,217,.22);margin-bottom:22px}
.star .en{color:var(--mute)} .star b{font-weight:normal;font-size:16px;letter-spacing:.2em;color:var(--mute)} .star em{font-style:normal;font-size:40px;letter-spacing:.1em;color:var(--amber)}
.cast{display:flex;gap:18px;align-items:center;margin-bottom:18px}
.hs{width:108px;height:128px;flex:none;background:var(--ink3);border:1px solid rgba(243,233,217,.25);border-radius:3px;position:relative;overflow:hidden}
.hs img{position:absolute;left:50%;transform:translateX(-50%);filter:drop-shadow(0 6px 10px rgba(0,0,0,.45))}
.hs .no{position:absolute;left:6px;top:5px;font-family:"Helvetica Neue",Helvetica,sans-serif;font-size:8px;letter-spacing:.15em;color:var(--amber);z-index:2}
.cast .tx{flex:1}
.cast .en{color:var(--mute);font-size:8.5px;letter-spacing:.24em}
.cast .actor{font-size:16px;letter-spacing:.12em;margin:7px 0 3px;color:var(--mute)}
.cast .actor span{font-size:13px;margin-left:4px}
.cast .role{font-size:25px;letter-spacing:.06em;line-height:1.25;color:var(--cream)}
.cast .line{font-size:13.5px;letter-spacing:.06em;color:var(--mute);margin-top:7px;line-height:1.55}
.credits{margin-top:26px;padding-top:20px;border-top:1px solid rgba(243,233,217,.22);display:grid;grid-template-columns:1fr 1fr 1fr;text-align:center}
.credits .en{display:block;color:var(--mute);font-size:8px;margin-bottom:6px}
.credits b{font-weight:normal;font-size:14.5px;letter-spacing:.1em}

/* S03 跑馬燈 */
#s03{padding:30px 0 32px}
.mq{position:relative;width:368px;height:150px;margin:0 auto;background:#9E2F28;border-radius:10px}
.mq .fr{position:absolute;inset:22px;border:2px solid #D8B66A;border-radius:4px}
.mq .fr2{position:absolute;inset:27px;border:1px solid rgba(216,182,106,.55);border-radius:2px}
.mq .t{position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);text-align:center;font-size:36px;letter-spacing:.16em;padding-left:.16em;
  background:linear-gradient(180deg,#FBE6A8 0%,#E9C77A 45%,#C99A45 100%);-webkit-background-clip:text;color:transparent}
.bulb{position:absolute;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:#6E2A1F;animation:chase .5s steps(1) infinite}
@keyframes chase{0%{background:#FFE7A6;box-shadow:0 0 6px 2px rgba(255,214,120,.75)}33.33%{background:#7A3325;box-shadow:none}100%{background:#7A3325;box-shadow:none}}
.mq .tag{position:absolute;left:50%;top:-11px;transform:translateX(-50%);background:var(--ink);padding:0 12px;color:#D8B66A}

/* S04 通告單 */
#s04{padding:40px 22px 44px}
.sheet{background:var(--paper);color:#2A201A;border-radius:3px;padding:22px 20px 24px;position:relative;box-shadow:0 10px 26px rgba(0,0,0,.35)}
.sheet .hd{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid #2A201A;padding-bottom:10px}
.sheet .hd .en{color:var(--red);font-size:9px}
.sheet .hd h3{font-weight:normal;font-size:28px;letter-spacing:.14em;margin-top:5px}
.sheet .hd .day{text-align:right}
.sheet .hd .day b{display:block;font-weight:normal;font-size:22px;letter-spacing:.04em;margin-top:4px}
.sheet .meta{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:6px 10px;padding:12px 88px 12px 0;border-bottom:1px solid rgba(42,32,26,.3);font-size:13.5px;letter-spacing:.06em}
.sheet .meta span{color:#8C7A68;margin-right:6px}
.sheet .row{display:flex;align-items:center;padding:13px 0;border-bottom:1px dashed rgba(42,32,26,.3)}
.sheet .row:last-of-type{border-bottom:none}
.sheet .tm{width:66px;font-size:21px;color:var(--red);letter-spacing:.02em}
.sheet .wh{flex:1}
.sheet .wh p{font-size:16px;letter-spacing:.06em}
.sheet .wh small{display:block;font-size:12.5px;color:#7D6C5C;letter-spacing:.05em;margin-top:3px}
.sheet .who{width:78px;text-align:center;font-size:13.5px;letter-spacing:.08em;border:1px solid #2A201A;border-radius:20px;padding:5px 0}
.stamp{position:absolute;right:2px;top:50%;margin-top:-38px;width:76px;height:76px;border:2px solid rgba(188,68,60,.85);border-radius:50%;transform:rotate(-14deg);color:rgba(188,68,60,.9);text-align:center;display:flex;flex-direction:column;justify-content:center}
.stamp b{font-weight:normal;font-size:15px;letter-spacing:.1em}
.stamp i{font-style:normal;font-family:"Helvetica Neue",Helvetica,sans-serif;font-size:7px;letter-spacing:.2em;margin-top:2px}
#s04 .note{margin-top:20px;font-size:15px;letter-spacing:.12em;color:var(--mute);line-height:1.7}

/* 場次 */
.scene{padding:36px 0 38px}
.slate{margin:0 26px;border-radius:4px;overflow:hidden;border:1px solid rgba(243,233,217,.3)}
.clap{height:20px;background:repeating-linear-gradient(-55deg,var(--cream) 0 14px,var(--ink) 14px 28px)}
.slate .g{display:grid;grid-template-columns:1fr 1fr 1.25fr;background:var(--ink2)}
.slate .g div{padding:8px 0 9px;text-align:center;border-left:1px solid rgba(243,233,217,.2)}
.slate .g div:first-child{border-left:none}
.slate .g .en{display:block;color:var(--mute);font-size:8px;margin-bottom:3px}
.slate .g b{font-weight:normal;font-size:20px;letter-spacing:.06em}
.scene .who{margin:20px 0 0;font-size:16px;letter-spacing:.12em;color:var(--mute)}
.scene .who em{font-style:normal;color:var(--amber);font-size:19px}
.scene h3{font-weight:normal;font-size:28px;line-height:1.42;letter-spacing:.06em;margin-top:10px}
.scene .desc{font-size:15px;line-height:1.75;letter-spacing:.06em;color:var(--mute);margin-top:12px}
.film{display:flex;margin:22px auto 0;width:384px;background:#0B0807;padding:10px 0;border-radius:2px}
.film .sp{width:27px;flex:none;background-image:linear-gradient(180deg,rgba(243,233,217,.5) 0 10px,transparent 10px 20px);background-size:8px 20px;background-repeat:repeat-y;background-position:center 4px}
.film .v{width:330px;height:412.5px;background-size:cover;background-position:center;border-radius:2px}
.parts{margin:20px 26px 0;border-top:1px solid rgba(243,233,217,.22)}
.parts div{display:flex;align-items:baseline;padding:11px 0;border-bottom:1px solid rgba(243,233,217,.22)}
.parts .en{width:62px;flex:none;color:var(--amber);font-size:8.5px;letter-spacing:.22em}
.parts p{font-size:15px;letter-spacing:.06em;line-height:1.5}

/* S09 選角 */
#s09{padding:42px 22px 40px}
#s09 h2{font-weight:normal;font-size:28px;letter-spacing:.1em;line-height:1.4;margin-top:10px}
#s09 .lead{font-size:14.5px;color:var(--mute);letter-spacing:.08em;margin-top:8px}
.cs{margin-top:22px;background:var(--ink2);border:1px solid rgba(243,233,217,.16);border-radius:4px;padding:14px 14px 14px}
.cs .h{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px}
.cs .h b{font-weight:normal;font-size:18px;letter-spacing:.1em}
.cs .h span{font-size:13.5px;color:var(--amber);letter-spacing:.1em}
.row5{display:flex;justify-content:space-between;align-items:flex-end;height:118px}
.row5 div{flex:1;text-align:center;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%}
.row5 img{max-width:64px;max-height:92px;filter:drop-shadow(0 5px 8px rgba(0,0,0,.5))}
.row5 p{font-size:11.5px;letter-spacing:.04em;margin-top:6px;color:var(--mute);white-space:nowrap}
.phs{display:flex;gap:10px;align-items:flex-start}
.phs .pw{width:62px;height:96px;overflow:hidden;flex:none}
.phs .pw img{width:62px;display:block}
.chips{display:flex;flex-wrap:wrap;gap:6px;align-content:flex-start;padding-top:4px}
.chips span{font-size:12.5px;letter-spacing:.05em;border:1px solid rgba(243,233,217,.35);border-radius:20px;padding:4px 9px}
.chips span.z{border-color:var(--amber);color:var(--amber)}
.ph5{height:132px;border-radius:3px;background-size:cover;background-position:center 58%}

/* S10 片尾彩蛋 */
#s10{padding:42px 0 40px}
#s10 .kk{font-size:17px;letter-spacing:.3em;color:var(--mute);margin-top:10px}
#s10 h2{font-weight:normal;font-size:29px;letter-spacing:.08em;line-height:1.42;margin-top:8px}
.lbx{margin:22px 0 0;background:#000;padding:22px 0}
.lbx div{height:268px;background-size:cover;background-position:center 8%}
.gifts{margin:22px 26px 0}
.gifts div{display:flex;align-items:center;padding:12px 0;border-bottom:1px solid rgba(243,233,217,.2)}
.gifts div:first-child{border-top:1px solid rgba(243,233,217,.2)}
.gifts .p{width:84px;flex:none;font-size:15.5px;letter-spacing:.06em}
.gifts .ar{width:22px;flex:none;color:var(--amber);font-family:"Helvetica Neue",Helvetica,sans-serif;font-size:12px}
.gifts .to{flex:1}
.gifts .to b{font-weight:normal;font-size:16px;letter-spacing:.06em;color:var(--amber)}
.gifts .to small{display:block;font-size:12.5px;color:var(--mute);letter-spacing:.05em;margin-top:3px}

/* S11 收尾 */
#s11{padding:40px 0 46px}
#s11 .film{margin-top:0}
#s11 h2{font-weight:normal;font-size:27px;letter-spacing:.06em;line-height:1.55;margin-top:28px}
.endc{margin:30px auto 0;width:250px;text-align:center}
.endc .clap{border-radius:3px 3px 0 0}
.endc .bd{background:var(--ink2);border:1px solid rgba(243,233,217,.3);border-top:none;padding:14px 0 14px;border-radius:0 0 3px 3px}
.endc b{font-weight:normal;font-size:30px;letter-spacing:.14em;padding-left:.14em}
.endc .en{display:block;color:var(--mute);margin-top:8px;font-size:8.5px}
"""


def hs(no, img, style):
    return f'<div class="hs"><span class="no">{no}</span><img src="img/{img}" style="{style}"></div>'


def scene(sid, no, tm, place, actor, role, h3, desc, clip, parts):
    p = ''.join(f'<div><span class="en">{k}</span><p>{v}</p></div>' for k, v in parts)
    return f'''<section id="{sid}" class="scene">
<div class="slate"><div class="clap"></div><div class="g"><div><span class="en">Scene</span><b>{no}</b></div><div><span class="en">Time</span><b>{tm}</b></div><div><span class="en">Set</span><b>{place}</b></div></div></div>
<p class="who c">{actor}　飾　<em>{role}</em></p>
<h3 class="c">{h3}</h3>
<p class="desc c">{desc}</p>
<div class="film"><div class="sp"></div><div class="v" data-clip="{clip}" style="background-image:url(gif/clips/{clip}/001.jpg)"></div><div class="sp"></div></div>
<div class="parts">{p}</div>
</section>'''


def bulbs(w=368, h=150, step=18.4):
    out = []; i = 0
    per = [(x, 11) for x in [11 + k * step for k in range(int((w - 22) / step) + 1)]]
    right = [(w - 11, y) for y in [11 + k * step for k in range(1, int((h - 22) / step) + 1)]]
    bot = [(x, h - 11) for x in [w - 11 - k * step for k in range(1, int((w - 22) / step) + 1)]]
    left = [(11, y) for y in [h - 11 - k * step for k in range(1, int((h - 22) / step))]]
    for x, y in per + right + bot + left:
        out.append(f'<i class="bulb" style="left:{x:.1f}px;top:{y:.1f}px;animation-delay:-{(i % 3) * 0.5 / 3:.4f}s"></i>'); i += 1
    return ''.join(out)


def build():
    s01 = '''<section id="s01" class="c">
<p class="en amber pre">Xunuanli Pictures Presents</p>
<p class="kick">煦暖曆全系列，一次到齊</p>
<h1>2027，<br>由你主演。</h1>
<p class="sub">這四位，是你一整年的<span class="hl">最佳配角</span></p>
<div class="strip"><div class="holes t"></div><div class="holes b"></div>
<div class="frames"><div style="background-image:url(img/o1.jpg)"></div><div style="background-image:url(img/o2.jpg)"></div><div style="background-image:url(img/o3.jpg)"></div><div style="background-image:url(img/o4.jpg)"></div></div></div>
<div class="names"><div><span class="en amber">01</span><b>實體日曆</b></div><div><span class="en amber">02</span><b>手機日曆</b></div><div><span class="en amber">03</span><b>手帳</b></div><div><span class="en amber">04</span><b>語錄卡</b></div></div>
<p class="tail">一份大禮包，演完你的一整年</p>
</section>'''

    cast = [
        ('No.01 · Desk Calendar', '實體日曆', '每天的開場白', '每天早上，第一個跟你說話的那一句。', hs('01', 'h_cal.png', 'height:112px;top:12px')),
        ('No.02 · Phone Calendar', '手機日曆', '口袋裡的老朋友', '你走到哪裡，它就跟到哪裡。', hs('02', 'h_ph.png', 'width:76px;top:16px')),
        ('No.03 · Planner', '手帳', '祕書兼樹洞', '白天幫你記事，晚上聽你說心事。', hs('03', 'h_pl.png', 'height:112px;top:12px')),
        ('No.04 · Quote Cards', '語錄卡', '替你說出口的人', '說不出口的話，就交給它。', hs('04', 'h_qt.png', 'width:92px;top:26px')),
    ]
    rows = ''.join(f'<div class="cast">{h}<div class="tx"><p class="en">{e}</p><p class="actor">{a}<span>飾</span></p><p class="role">{r}</p><p class="line">{l}</p></div></div>' for e, a, r, l, h in cast)
    s02 = f'''<section id="s02">
<p class="en amber c">The Cast</p><h2 class="c">演員表</h2>
<div class="star"><span class="en">Starring</span><b>主演</b><em>你</em></div>
{rows}
<div class="credits"><div><span class="en">Director</span><b>你自己</b></div><div><span class="en">Screenplay</span><b>你的 2027</b></div><div><span class="en">Studio</span><b>煦暖曆</b></div></div>
</section>'''

    s03 = f'''<section id="s03"><div class="mq">{bulbs()}<div class="fr"></div><div class="fr2"></div><div class="t">聖誕節前到貨</div></div></section>'''

    sheet_rows = [('07:30', '書桌前，撕下今天', '讀一句寫給你的話，再出門', '實體日曆'),
                  ('08:40', '通勤路上，解鎖手機', '今天那一句，已經在桌面等你', '手機日曆'),
                  ('14:00', '午後咖啡廳，攤開一週', '排行程、打勾、記下小事', '手帳'),
                  ('22:30', '睡前床邊，抽一張卡', '給今天的自己，一句晚安', '語錄卡')]
    sr = ''.join(f'<div class="row"><div class="tm">{t}</div><div class="wh"><p>{a}</p><small>{b}</small></div><div class="who">{w}</div></div>' for t, a, b, w in sheet_rows)
    s04 = f'''<section id="s04">
<div class="sheet">
<div class="hd"><div><p class="en">Call Sheet</p><h3>2027 通告單</h3></div><div class="day"><p class="en">Day</p><b>001 / 365</b></div></div>
<div class="meta"><p><span>劇名</span>好好生活</p><p><span>主演</span>你</p><p><span>開拍</span>1 月 1 日</p><p><span>殺青</span>12 月 31 日</p><div class="stamp"><b>每天開拍</b><i>365 Days</i></div></div>
{sr}
</div>
<p class="note c">一天四場戲，四個角色輪流上場<br>你只要負責，好好過今天</p>
</section>'''

    s05 = scene('s05', '01', '07:30', '書桌', '實體日曆', '每天的開場白',
                '撕下昨天，<br>今天第一句話是寫給你的', '早上第一眼看見的不是訊息，<br>是一句讓你想好好過今天的話。', 'x_tear',
                [('Daily', '一天一頁，陪你 365 天'), ('Choose', '五款任選：煦暖曆、幹話曆、鮮花圖鑑、<br>旅行機票、日日法華')])
    s06 = scene('s06', '02', '08:40', '走到哪', '手機日曆', '口袋裡的老朋友',
                '出了門，<br>今天那句話還跟著你', '上班、出差、午休，<br>解鎖手機就看得到，不怕忘記撕。', 'c_where',
                [('Widget', '桌面小工具，三種尺寸任你放'), ('Choose', '十六款任選，iOS、Android 都能用')])
    s07 = scene('s07', '03', '14:00', '咖啡廳', '手帳', '祕書兼樹洞',
                '白天替你記行程，<br>晚上聽你說心事', '開會、待辦、生活小事排在同一頁，<br>每個月還陪你問問自己，過得好嗎？', 'p_week',
                [('Plan', '週計畫、月計畫、年計畫，一本排好'), ('Reflect', '12 個自我覺察主題，寫給自己看')])
    s08 = scene('s08', '04', '22:30', '床邊', '語錄卡', '替你說出口的人',
                '累的時候，抽一張給自己<br>說不出口的，抽一張給他', '一張卡，一句剛剛好的話，<br>今天的情緒，有地方放了。', 'q_draw',
                [('Cards', '45 張中英雙語語錄卡'), ('NFC', '手機碰一下收藏盒，看每張卡的延伸解讀')])

    cal = ''.join(f'<div><img src="img/{f}.png" style="{'max-width:80px' if f=='c_tr' else ''}"><p>{n}</p></div>' for f, n in [('c_xn', '煦暖曆'), ('c_gh', '幹話曆'), ('c_fl', '鮮花圖鑑'), ('c_tr', '旅行機票'), ('c_fh', '日日法華')])
    pls = ''.join(f'<div><img src="img/{f}.png" style="max-height:96px"><p>{n}</p></div>' for f, n in [('pl_d', '晨曦米白'), ('pl_a', '沙丘暖杏'), ('pl_b', '靜海霧藍'), ('pl_c', '森語墨綠')])
    s09 = f'''<section id="s09">
<p class="en amber c">Casting</p>
<h2 class="c">每個角色的造型，<br>由你來挑</h2>
<p class="lead c">四個角色都能選款式，挑成你最喜歡的樣子</p>
<div class="cs"><div class="h"><b>實體日曆</b><span>五款選一</span></div><div class="row5">{cal}</div></div>
<div class="cs"><div class="h"><b>手機日曆</b><span>十六款選一</span></div>
<div class="phs"><div class="pw"><img src="img/ph_xn.png"></div><div class="pw"><img src="img/ph_gh.png"></div><div class="pw"><img src="img/ph_tr.png"></div>
<div class="chips"><span>煦暖曆</span><span>旅行曆</span><span>鮮花圖鑑</span><span>幹話曆</span><span class="z">12 星座曆</span></div></div></div>
<div class="cs"><div class="h"><b>手帳</b><span>開窗款、素面款，各四色</span></div><div class="row5" style="height:110px">{pls}</div></div>
<div class="cs"><div class="h"><b>語錄卡</b><span>五色收藏盒</span></div><div class="ph5" style="background-image:url(img/qt5.jpg)"></div></div>
</section>'''

    gifts = [('實體日曆', '送天天見面的同事', '每撕一頁，就想起你一次'),
             ('手機日曆', '送住在遠方的朋友', '轉寄一封兌換碼，人在國外也收得到'),
             ('語錄卡', '送最懂你的好朋友', '那句說不出口的話，讓卡片替你說'),
             ('手帳', '留給自己', '2027，記得好好照顧自己')]
    g = ''.join(f'<div><span class="p">{a}</span><span class="ar">→</span><span class="to"><b>{b}</b><small>{c}</small></span></div>' for a, b, c in gifts)
    s10 = f'''<section id="s10">
<p class="en amber c">Post-credits Scene</p>
<p class="kk c">片尾彩蛋</p>
<h2 class="c">一份大禮包，<br>也能拆成四份心意</h2>
<div class="lbx"><div style="background-image:url(img/gift.jpg)"></div></div>
<div class="gifts">{g}</div>
</section>'''

    s11 = '''<section id="s11">
<div class="film"><div class="sp"></div><div class="v" style="background-image:url(img/end.jpg)"></div><div class="sp"></div></div>
<h2 class="c">你負責好好生活，<br>提醒、記錄、打氣，<br>交給它們。</h2>
<div class="endc"><div class="clap"></div><div class="bd"><b>2027，開拍</b><span class="en">Take 1 · Jan 1, 2027</span></div></div>
</section>'''

    html = f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{s01}{s02}{s03}{s04}{s05}{s06}{s07}{s08}{s09}{s10}{s11}</body></html>'
    open(f'{D}/page.html', 'w').write(html)
    print('page.html', len(html))


if __name__ == '__main__':
    build()
