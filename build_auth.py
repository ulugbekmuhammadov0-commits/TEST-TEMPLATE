import os
from partials import page

def write(path, title, body, active=None, guard=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(page(title, body, active, guard))
    print(path, len(body))

PHOTO_BLOCK = '''<div class="auth-photo" style="background-image:url(assets/img/airplane.jpg)">
<div class="ov"></div>
<div class="q"><b>Your journey. We find the way.</b><span>Join 2M+ travellers who let BTicket find their tickets.</span></div>
</div>'''

REGISTER = '''
<div class="auth-wrap">
''' + PHOTO_BLOCK + '''
<div class="auth-form">
<div class="auth-card" id="regCard">
<a class="logo" href="./"><span class="logo-mark">B</span>BTicket</a>
<h1>Start your journey with BTicket.</h1>
<p class="sub">Create an account and let us find your next ticket.</p>
<form id="regForm" novalidate>
  <div class="fieldx"><label for="r-first">First name</label><input id="r-first" type="text" autocomplete="given-name" /><div class="fe" id="fe-first"></div></div>
  <div class="fieldx"><label for="r-last">Last name</label><input id="r-last" type="text" autocomplete="family-name" /><div class="fe" id="fe-last"></div></div>
  <div class="fieldx"><label for="r-email">Email</label><input id="r-email" type="email" autocomplete="email" /><div class="fe" id="fe-email"></div></div>
  <div class="fieldx"><label for="r-phone">Phone number</label><input id="r-phone" type="tel" autocomplete="tel" placeholder="+998 90 000 00 00" /><div class="fe" id="fe-phone"></div></div>
  <div class="fieldx"><label for="r-pass">Password</label>
    <div class="pw-wrap"><input id="r-pass" type="password" autocomplete="new-password" />
    <button class="pw-toggle" type="button" data-toggle="r-pass" aria-label="Show password">👁</button></div>
    <div class="fe" id="fe-pass"></div></div>
  <div class="fieldx"><label for="r-pass2">Confirm password</label>
    <div class="pw-wrap"><input id="r-pass2" type="password" autocomplete="new-password" />
    <button class="pw-toggle" type="button" data-toggle="r-pass2" aria-label="Show password">👁</button></div>
    <div class="fe" id="fe-pass2"></div></div>
  <label class="terms"><input type="checkbox" id="r-terms" />
  <span>I agree to the <a href="../support/" style="color:var(--blue);font-weight:700">Terms</a> and <a href="../support/" style="color:var(--blue);font-weight:700">Privacy Policy</a>.</span></label>
  <div class="fe" id="fe-terms"></div>
  <button class="btn-cta lg auth-submit" type="submit" id="r-submit">Create account</button>
</form>
<div class="or">OR</div>
<div class="social">
  <button type="button" id="r-google">Continue with Google</button>
  <button type="button" id="r-apple">Continue with Apple</button>
</div>
<div class="auth-alt">Already have an account? <a href="login/" id="toLogin">Sign in</a></div>
</div>
<div class="auth-card success-box" id="regSuccess" style="display:none">
  <div class="tick">✓</div>
  <h2>Account created!</h2>
  <p>Welcome aboard — taking you back to your search…</p>
</div>
</div>
</div>
<script>
document.querySelectorAll(".pw-toggle").forEach(b => b.addEventListener("click", () => {
  const inp = document.getElementById(b.dataset.toggle);
  inp.type = inp.type === "password" ? "text" : "password";
  b.textContent = inp.type === "password" ? "👁" : "🙈";
}));
function setErr(id, msg){ document.getElementById("fe-" + id).textContent = msg || ""; }
function bad(id, isBad){ document.getElementById(id).classList.toggle("bad", !!isBad); }
document.getElementById("regForm").addEventListener("submit", function(e){
  e.preventDefault();
  const first = document.getElementById("r-first").value.trim();
  const last = document.getElementById("r-last").value.trim();
  const email = document.getElementById("r-email").value.trim();
  const phone = document.getElementById("r-phone").value.trim();
  const pass = document.getElementById("r-pass").value;
  const pass2 = document.getElementById("r-pass2").value;
  const terms = document.getElementById("r-terms").checked;
  let ok = true;
  [[ "first", first.length >= 1 ], [ "last", last.length >= 1 ], [ "email", /^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(email) ],
   [ "phone", phone.replace(/\\D/g, "").length >= 7 ], [ "pass", pass.length >= 6 ], [ "pass2", pass2 === pass && pass2.length > 0 ],
   [ "terms", terms ]].forEach(([id, valid]) => { setErr(id, valid ? "" : ({ first:"Enter your first name", last:"Enter your last name",
    email:"Enter a valid email address", phone:"Enter a valid phone number", pass:"Password must be at least 6 characters",
    pass2:"Passwords do not match", terms:"Please accept the Terms to continue" })[id]);
    if (id !== "terms") bad("r-" + id.replace("pass2","pass2") === "r-pass2" ? "r-pass2" : "r-" + id, !valid);
    ok = ok && valid; });
  bad("r-pass2", pass2 !== pass || !pass2);
  if (!ok) return;
  const btn = document.getElementById("r-submit");
  btn.disabled = true; btn.textContent = "Creating account…";
  setTimeout(() => {
    btSave({ first: first, last: last, email: email, phone: phone });
    document.getElementById("regCard").style.display = "none";
    document.getElementById("regSuccess").style.display = "block";
    const ret = sessionStorage.getItem("bticket_return");
    sessionStorage.removeItem("bticket_return");
    setTimeout(() => { location.href = ret || (window.BT_ROOT + "flights/"); }, 1300);
  }, 900);
});
["r-google","r-apple"].forEach(id => document.getElementById(id).addEventListener("click", () => {
  btSave({ first: "Traveller", email: "social@bticket.uz" });
  const ret = sessionStorage.getItem("bticket_return");
  sessionStorage.removeItem("bticket_return");
  location.href = ret || (window.BT_ROOT + "flights/");
}));
</script>'''
write("register/index.html", "Create account — BTicket", REGISTER)

LOGIN = '''
<div class="auth-wrap">
''' + PHOTO_BLOCK + '''
<div class="auth-form">
<div class="auth-card" id="logCard">
<a class="logo" href="./"><span class="logo-mark">B</span>BTicket</a>
<h1>Welcome back.</h1>
<p class="sub">Sign in to continue your journey.</p>
<form id="logForm" novalidate>
  <div class="fieldx"><label for="l-email">Email</label><input id="l-email" type="email" autocomplete="email" /><div class="fe" id="fe-lemail"></div></div>
  <div class="fieldx"><label for="l-pass">Password</label>
    <div class="pw-wrap"><input id="l-pass" type="password" autocomplete="current-password" />
    <button class="pw-toggle" type="button" data-toggle="l-pass" aria-label="Show password">👁</button></div>
    <div class="fe" id="fe-lpass"></div></div>
  <div style="display:flex;justify-content:space-between;align-items:center;margin-top:14px">
    <label class="checkrow" style="margin-top:0"><input type="checkbox" id="l-remember" checked /> Remember me</label>
    <a href="#" style="color:var(--blue);font-weight:700;font-size:.9rem" id="l-forgot">Forgot password?</a>
  </div>
  <button class="btn-cta lg auth-submit" type="submit" id="l-submit">Sign in</button>
</form>
<div class="or">OR</div>
<div class="social">
  <button type="button" id="l-google">Continue with Google</button>
  <button type="button" id="l-apple">Continue with Apple</button>
</div>
<div class="auth-alt">Don't have an account? <a href="register/">Create account</a></div>
</div>
</div>
</div>
<script>
document.querySelectorAll(".pw-toggle").forEach(b => b.addEventListener("click", () => {
  const inp = document.getElementById(b.dataset.toggle);
  inp.type = inp.type === "password" ? "text" : "password";
  b.textContent = inp.type === "password" ? "👁" : "🙈";
}));
document.getElementById("l-forgot").addEventListener("click", e => {
  e.preventDefault();
  document.getElementById("l-forgot").textContent = "Password reset link sent ✉";
});
document.getElementById("logForm").addEventListener("submit", function(e){
  e.preventDefault();
  const email = document.getElementById("l-email").value.trim();
  const pass = document.getElementById("l-pass").value;
  let ok = true;
  const em = /^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(email);
  document.getElementById("fe-lemail").textContent = em ? "" : "Enter a valid email address";
  document.getElementById("l-email").classList.toggle("bad", !em);
  const pv = pass.length >= 6;
  document.getElementById("fe-lpass").textContent = pv ? "" : "Password must be at least 6 characters";
  document.getElementById("l-pass").classList.toggle("bad", !pv);
  ok = em && pv;
  if (!ok) return;
  const btn = document.getElementById("l-submit");
  btn.disabled = true; btn.textContent = "Signing in…";
  setTimeout(() => {
    btSave({ first: email.split("@")[0], email: email });
    const ret = sessionStorage.getItem("bticket_return");
    sessionStorage.removeItem("bticket_return");
    location.href = ret || (window.BT_ROOT + "flights/");
  }, 900);
});
["l-google","l-apple"].forEach(id => document.getElementById(id).addEventListener("click", () => {
  btSave({ first: "Traveller", email: "social@bticket.uz" });
  const ret = sessionStorage.getItem("bticket_return");
  sessionStorage.removeItem("bticket_return");
  location.href = ret || (window.BT_ROOT + "flights/");
}));
</script>'''
write("login/index.html", "Sign in — BTicket", LOGIN)

