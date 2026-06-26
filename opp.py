from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import User, users_db, menu_items, JazzCashPayment, CreditCardPayment, PayPalPayment

app = Flask(__name__)
app.secret_key = "rise_dine_pro_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth', methods=['POST'])
def auth():
    action = request.form.get('action')
    u, p = request.form.get('username'), request.form.get('password')
    if action == 'register':
        if u not in users_db:
            users_db[u] = User(u, p)
            flash("Account created! Please login.")
        return redirect(url_for('index'))
    user = users_db.get(u)
    if user and user.password == p:
        session['user'] = u
        return redirect(url_for('dashboard'))
    flash("Invalid credentials")
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session: return redirect(url_for('index'))
    q = request.args.get('search', '').lower()
    items = [i for i in menu_items if q in i.name.lower()] if q else menu_items
    return render_template('dashboard.html', menu=items)

@app.route('/add/<int:id>')
def add(id):
    item = next((i for i in menu_items if i.item_id == id), None)
    if item: users_db[session['user']].cart.append(item)
    return redirect(url_for('dashboard'))

@app.route('/cart')
def cart():
    u = users_db[session['user']]
    return render_template('cart.html', cart=u.cart, total=sum(i.price for i in u.cart))

@app.route('/pay', methods=['POST'])
def pay():
    m = request.form.get('method')
    u = users_db[session['user']]
    p = JazzCashPayment() if m == "JazzCash" else CreditCardPayment() if m == "Card" else PayPalPayment()
    msg = p.pay(sum(i.price for i in u.cart))
    u.cart = []
    return render_template('receipt.html', msg=msg)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)