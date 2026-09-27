import os
from partials import page, phero

def write(path, title, body, active=None, guard=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(page(title, body, active, guard))
    print(path, len(body))

# ============ HOW IT WORKS ============
HW = phero("How BTicket works", "A detailed look at the automated system that searches, monitors, finds and notifies for you.", "How it works")
HW += '''
<div class="container" style="padding-bottom:56px">
<div class="sec-head left" style="margin-left:0"><h2 style="font-size:1.6rem">The full journey</h2><p>Eight transparent steps between you and your trip.</p></div>
<div class="journey">
<div class="jstep"><div class="num">01</div><b>Tell us where</b><p>Tell us where you want to go.</p></div>
<div class="jstep"><div class="num">02</div><b>Preferences</b><p>Choose your preferences.</p></div>
<div class="jstep"><div class="num">03</div><b>We search</b><p>BTicket searches available tickets.</p></div>
<div class="jstep"><div class="num">04</div><b>We monitor</b><p>If needed, BTicket monitors availability.</p></div>
<div class="jstep"><div class="num">05</div><b>Match found</b><p>A matching ticket is found.</p></div>
<div class="jstep"><div class="num">06</div><b>Notification</b><p>You receive a notification.</p></div>
<div class="jstep"><div class="num">07</div><b>Request booking</b><p>You can request booking.</p></div>
<div class="jstep"><div class="num">08</div><b>Ready</b><p>Your journey is ready.</p></div>
</div>
<div class="bf-strip" style="margin-top:34px">
<div class="bf on"><span class="be">🔍</span>SEARCH</div>
<div class="bf on"><span class="be">📋</span>RESULTS</div>
<div class="bf on"><span class="be">🎯</span>SELECT</div>
<div class="bf on"><span class="be">🧾</span>BREAKDOWN</div>
<div class="bf"><span class="be">👤</span>PASSENGER</div>
<div class="bf"><span class="be">💳</span>PAYMENT</div>
<div class="bf"><span class="be">✅</span>CONFIRMATION</div>
<div class="bf"><span class="be">🎟</span>TICKET</div>
</div>
<div class="sec-head left" style="margin:44px 0 20px"><h2 style="font-size:1.6rem">Monitoring & notifications</h2></div>
<div class="feat-grid">
<div class="feat"><div class="ico">🤖</div><b>Automatic search</b><p>Let BTicket keep looking for your preferred ticket.</p></div>
<div class="feat"><div class="ico">🔔</div><b>Real-time notifications</b><p>Know the moment a matching ticket becomes available.</p></div>
<div class="feat"><div class="ico">🌐</div><b>Flights + Trains</b><p>One platform for different ways to travel.</p></div>
<div class="feat"><div class="ico">💳</div><b>Transparent pricing</b><p>Ticket price and service fee are always separate.</p></div>
<div class="feat"><div class="ico">🔒</div><b>Secure payments</b><p>Protected payment experience.</p></div>
<div class="feat"><div class="ico">🎯</div><b>Smart search</b><p>Set your route, date, budget and preferences.</p></div>
</div>
<div class="price-grid" style="margin-top:40px">
<div class="bill">
<h3>Example price breakdown</h3>
<div class="brow"><span>Ticket price</span><b>100,000 UZS</b></div>
<div class="brow"><span>Notification service <span class="mut">(10%)</span></span><b>10,000 UZS</b></div>
<div class="brow"><span>Booking service <span class="mut">(10%)</span></span><b>10,000 UZS</b></div>
<div class="brow total"><span>Total</span><b>120,000 UZS</b></div>
<div class="fee-note">= 20% total service fees, always shown upfront</div>
</div>
<div>
<div class="search-card">
<span class="status green"><span class="p-dot"></span>Automatic search active</span>
<div class="route" style="margin-top:12px">Tashkent → Dubai</div>
<div class="meta2">27 September 2026 • 1 passenger</div>
<div class="kv" style="border:none"><span>Budget</span><b>Up to $300</b></div>
<div class="checks"><div>✓ Any suitable flight</div><div>✓ Notify when found</div><div>✓ Monitor availability</div></div>
</div>
</div>
</div>
</div>'''
write("how-it-works/index.html", "How it works — BTicket", HW, "How it works")

# ============ SUPPORT ============
SU = phero("Support", "Questions about searches, monitoring or bookings? We are here 24/7.", "Support")
SU += '''
<div class="container" style="padding-bottom:56px">
<div class="contact-chips">
<div class="contact-chip"><b>✈ Telegram</b><p>Fastest way to reach us — our bot answers in seconds.</p><span class="go">@bticket_bot →</span></div>
<div class="contact-chip"><b>✉ Email</b><p>Detailed requests and documents.</p><span class="go">support@bticket.uz →</span></div>
<div class="contact-chip"><b>☎ Phone</b><p>24/7 hotline.</p><span class="go">+998 71 200 00 00 →</span></div>
<div class="contact-chip"><b>📷 Instagram</b><p>News, routes and special offers.</p><span class="go">@bticket.uz →</span></div>
</div>
<div class="sec-head left" style="margin:44px 0 16px"><h2 style="font-size:1.6rem">Help centre</h2></div>
<div class="faq">
<div class="q">How does automatic search work? <span>▾</span></div>
<div class="a">You set your route, date, budget and preferences. BTicket searches available flights and trains and keeps monitoring when your ticket isn’t available yet.</div>
<div class="q">What happens when a ticket is found? <span>▾</span></div>
<div class="a">You instantly receive a notification on the app, Telegram or email with the route, price and service fee. You can review and book in one tap.</div>
<div class="q">Are service fees transparent? <span>▾</span></div>
<div class="a">Always. The ticket price and the BTicket service fee (10–20%, depending on your plan) are shown separately before payment.</div>
<div class="q">Can I pause or cancel a search? <span>▾</span></div>
<div class="a">Yes — from Active searches you can pause or cancel any monitored search at any time.</div>
<div class="q">How do refunds work? <span>▾</span></div>
<div class="a">Refunds follow the carrier’s policy; the unused BTicket service fee is returned in full. See the refund policy for details.</div>
</div>
</div>
<script>
document.querySelectorAll(".faq .q").forEach(q => q.addEventListener("click", () => q.classList.toggle("open")));
</script>'''
write("support/index.html", "Support — BTicket", SU)

# ============ PROFILE ============
PR = phero("Profile", "Passengers, payment methods, preferences and settings.", "Profile")
PR += '''
<div class="container" style="padding-bottom:56px">
<div class="profile-two">
<div class="panel-card">
<h3>👥 Saved passengers</h3>
<div class="passenger"><div class="pv">UM</div><div><b>Ulugbek M.</b><div style="color:var(--mut);font-size:.83rem">Passport • preferred window seat</div></div><button class="btn-sm" style="margin-left:auto" type="button">Edit</button></div>
<div class="passenger"><div class="pv">AS</div><div><b>Aziza S.</b><div style="color:var(--mut);font-size:.83rem">Passport • preferred aisle seat</div></div><button class="btn-sm" style="margin-left:auto" type="button">Edit</button></div>
<button class="btn-outline" style="width:100%;margin-top:14px" type="button">+ Add passenger</button>
</div>
<div class="panel-card">
<h3>💳 Payment methods</h3>
<div class="kv" style="border:none"><span>HUMO •••• 4412</span><b style="color:var(--green)">Default</b></div>
<div class="kv" style="border:none"><span>VISA •••• 9087</span><b>—</b></div>
<button class="btn-outline" style="width:100%;margin-top:14px" type="button">+ Add payment method</button>
</div>
</div>
<div class="panel-card" style="margin-top:20px">
<h3>🎯 Preferred ticket settings</h3>
<div class="tabs">
<button class="tab active" data-ptab="pflight" type="button">✈ Flight preferences</button>
<button class="tab" data-ptab="ptrain" type="button">🚆 Train preferences</button>
</div>
<div class="panel active" id="ppflight">
<div class="pref-rows">
<div class="pref"><small>DEPARTURE TIME</small><select><option>Any time</option><option>Morning</option><option>Evening</option></select></div>
<div class="pref"><small>MAXIMUM PRICE</small><select><option>Up to $300</option><option>Up to $400</option></select></div>
<div class="pref"><small>AIRLINE PREFERENCE</small><select><option>Any airline</option><option>Uzbekistan Airways</option></select></div>
<div class="pref"><small>NUMBER OF STOPS</small><select><option>Direct only</option><option>Up to 1 stop</option></select></div>
<div class="pref"><small>BAGGAGE</small><select><option>1 checked bag</option><option>Carry-on only</option></select></div>
<div class="pref"><small>CLASS</small><select><option>Economy</option><option>Business</option></select></div>
</div>
</div>
<div class="panel" id="pptrain">
<div class="pref-rows">
<div class="pref"><small>TRAIN TYPE</small><select><option>Afrosiyob (high-speed)</option><option>Any</option></select></div>
<div class="pref"><small>COACH / CLASS</small><select><option>Economy class</option><option>Business class</option></select></div>
<div class="pref"><small>SEAT PREFERENCE</small><select><option>Window</option><option>Aisle</option></select></div>
<div class="pref"><small>DEPARTURE TIME</small><select><option>Any time</option><option>Morning</option></select></div>
</div>
</div>
<button class="btn-cta lg" style="width:100%;margin-top:16px" type="button">Save preferences</button>
</div>
<div class="panel-card" style="margin-top:20px">
<h3>⚙ Settings</h3>
<div class="kv" style="border:none"><span>Language</span><b>English</b></div>
<div class="kv" style="border:none"><span>Currency</span><b>UZS</b></div>
<div class="kv" style="border:none"><span>Notifications</span><b>Push • Telegram • Email</b></div>
<div class="kv" style="border:none"><span>Security</span><b>2FA enabled</b></div>
<button class="btn-outline" style="width:100%;margin-top:16px;color:var(--red);border-color:#f9c8cd" type="button" onclick="btOut()">Sign out</button>
</div>
</div>
<script>
document.querySelectorAll("[data-ptab]").forEach(t => t.addEventListener("click", () => {
  document.querySelectorAll("[data-ptab]").forEach(x => x.classList.remove("active"));
  document.querySelectorAll("#ppflight, #pptrain").forEach(x => x.classList.remove("active"));
  t.classList.add("active");
  document.getElementById("p" + t.dataset.ptab).classList.add("active");
}));
</script>'''
write("profile/index.html", "Profile — BTicket", PR, guard=True)
