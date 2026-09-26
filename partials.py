CSS = "assets/css/style.css"

BASE_SCRIPT = '''<script>
(function(){
  var d = location.pathname.split('/').filter(Boolean);
  var last = d[d.length - 1] || '';
  var dirs = ['flights','trains','active-searches','my-bookings','notifications','how-it-works','support','profile'];
  if (last && (/\\.[a-z]+$/i.test(last) || dirs.indexOf(last) !== -1)) d.pop();
  var root = '/' + d.join('/') + (d.length ? '/' : '');
  document.write('<base href="' + root + '">');
  document.write('<link rel="icon" type="image/svg+xml" href="' + root + 'assets/img/favicon.svg" />');
  document.write('<link rel="stylesheet" href="' + root + 'assets/css/style.css" />');
})();
</script>'''

def header(active=None):
    def l(href,label):
        act = ' class="active"' if active == label else ""
        return f'<a href="{href}"{act}>{label}</a>'
    return f'''<nav class="nav"><div class="container nav-in">
<a class="logo" href="./"><span class="logo-mark">B</span>BTicket</a>
<div class="links">{l("flights/","Flights")}{l("trains/","Trains")}{l("how-it-works/","How it works")}
</div>
<div class="nav-right">
<button class="pill" type="button">EN ▾</button>
<button class="pill" type="button">UZS ▾</button>
<button class="btn-outline" type="button">Sign in</button>
<a class="btn-cta" style="text-decoration:none;display:inline-block" href="profile/">Get started</a>
</div>
</div></nav>'''

def footer():
    return '''<footer><div class="container">
<div class="foot-cols">
<div>
<a class="logo" href="./"><span class="logo-mark">B</span>BTicket</a>
<p style="color:var(--mut);font-size:.9rem;margin-top:10px">Your journey. We find the way.</p>
<div style="margin-top:14px">
<a href="#">Telegram</a><a href="#">Instagram</a><a href="#">support@bticket.uz</a><a href="#">+998 71 200 00 00</a>
</div>
</div>
<div><div class="fc-t">Product</div><a href="flights/">Flights</a><a href="trains/">Trains</a><a href="how-it-works/">How it works</a><a href="support/">Support</a></div>
<div><div class="fc-t">Legal</div><a href="support/">Terms</a><a href="support/">Privacy</a><a href="support/">Refund policy</a></div>
<div><div class="fc-t">Account</div><a href="my-bookings/">My bookings</a><a href="notifications/">Notifications</a><a href="active-searches/">Active searches</a><a href="profile/">Profile</a></div>
</div>
<div class="foot-bottom"><span>© 2026 BTicket. All rights reserved.</span><span>Made in Uzbekistan 🇺🇿</span></div>
</div></footer>'''

def page(title, body, active=None):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
{BASE_SCRIPT}
</head>
<body>
{header(active)}
{body}
{footer()}
</body>
</html>'''

def phero(title, sub, crumb=None):
    c = f'<div class="crumbs"><a href="./">Home</a> → {crumb}</div>' if crumb else ""
    return f'''<div class="container phero">{c}<h1>{title}</h1><p>{sub}</p></div>'''

def search_widget(idpfx, cities_from, cities_to, btn):
    opts = lambda cities: "".join(f"<option>{c}</option>" for c in cities)
    return f'''<div class="widget-in">
<div class="fields">
<div class="field"><small>FROM</small><select id="{idpfx}-from">{opts(cities_from)}</select></div>
<button class="swap" data-swap="{idpfx}" type="button">⇄</button>
<div class="field"><small>TO</small><select id="{idpfx}-to">{opts(cities_to)}</select></div>
<div class="field"><small>DATE</small><input id="{idpfx}-date" type="date" value="2026-09-27" /></div>
<div class="field"><small>PASSENGERS</small><select id="{idpfx}-pax"><option>1 Adult</option><option>2 Adults</option><option>3 Adults</option></select></div>
</div>
<button class="btn-cta lg" style="width:100%;margin-top:16px" type="button" id="{btn}">Search tickets →</button>
<div class="err" id="{idpfx}-err"></div>
</div>
<div id="{idpfx}-loading" style="display:none;margin-top:16px"><div class="loader-box"><div class="spinner"></div><h2>Searching the best options…</h2></div></div>
<div id="{idpfx}-results" style="display:none;margin-top:16px" class="res-grid">
<aside class="filters" id="{idpfx}-filters">
<b style="font-size:.95rem">Filters</b>
<small>PRICE</small>
<select class="flt-sort" data-set="{idpfx}"><option value="asc">Price: low → high</option><option value="desc">Price: high → low</option></select>
<small>STOPS / CLASS</small>
<label class="frow"><input type="checkbox" class="flt-direct" data-set="{idpfx}" /> Direct only</label>
<small>BAGGAGE</small>
<label class="frow"><input type="checkbox" class="flt-bag" data-set="{idpfx}" checked /> Checked bag included</label>
<small>DEPARTURE</small>
<select class="flt-dep" data-set="{idpfx}"><option value="any">Any time</option><option value="am">Morning (before 12:00)</option><option value="pm">Afternoon / evening</option></select>
</aside>
<div id="{idpfx}-tickets"></div>
</div>'''
