import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology, login_required, lookup, usd


# export API_KEY=pk_598298c241a948fe908b77dc4159b4d6


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///discuss.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    id = session["user_id"]
    infos = db.execute("SELECT symbol, name, SUM(shares) as shares, price FROM ledger WHERE user_id = ? GROUP BY symbol", id)
    balance = db.execute("SELECT cash FROM users WHERE id = ?", id)
    cash = balance[0]["cash"]
    sum = 0
    for info in infos:
        sum += info["shares"] * info["price"]

    return render_template("index.html", infos=infos, cash=round(cash, 2), total=round((sum+cash), 2))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if not request.method == "POST":
        return render_template("buy.html")
    symbol = request.form.get("symbol")
    shares = request.form.get("shares")

    if not symbol:
        return apology("Please Enter a symbol", 400)

    if not shares:
        return apology("Please Enter number of shares", 400)
    if not shares.isnumeric():
        return apology("Please Enter a Positive whole number", 400)
    shares = float(shares)
    if shares < 1 or not shares.is_integer():
        return apology("Please Enter a Positive whole number", 400)
    shares = int(shares)
    stock = lookup(symbol)
    if not stock:
        return apology("Please Enter a Valid Symbol", 400)

    price = stock["price"]
    cost = price * int(shares)

    id = session["user_id"]
    balance = db.execute("SELECT cash FROM users WHERE id = ?", id)[0]

    if cost > float(balance["cash"]):
        return apology("Not Enough Cash", 400)

    new_cash = balance["cash"] - cost

    db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, id)
    time = datetime.now()
    db.execute("INSERT INTO ledger (user_id, symbol, name, shares, price, date) VALUES(? ,? ,? ,? ,?, ? )",
               session["user_id"], stock["symbol"], stock["name"], shares, stock["price"], time)
    flash("BOUGHT!")
    return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    id = session["user_id"]
    data = db.execute("SELECT * FROM ledger WHERE user_id = ?", id)
    return render_template("history.html", infos=data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/reset", methods=["GET", "POST"])
@login_required
def reset():
    """Change User password"""
    if request.method == "GET":
        return render_template("reset.html")
    id = session["user_id"]
    psw = request.form.get("pass")
    cpsw = request.form.get("confirm")

    if not psw or not cpsw:
        return apology("Please complete the given fields", 403)

    if not psw == cpsw:
        return apology("Password was not same as confirmation", 403)

    hash = generate_password_hash(psw)
    db.execute("UPDATE users SET hash = ? WHERE id = ?", hash, id)

    session.clear()
    flash("Changed")
    return redirect("/")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if not request.method == "POST":
        return render_template("quote.html")

    symbol = request.form.get("symbol")
    quote = lookup(symbol)

    if not quote:
        return apology("INVALID SYMBOL", 400)
    return render_template("quoted.html", quote=quote)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        user = request.form.get("username")
        psw = request.form.get("password")
        cpsw = request.form.get("confirmation")

        if not user or not psw or not cpsw:
            return apology("Please complete the given fields", 400)

        if not psw == cpsw:
            return apology("Password was not same as confirmation", 400)

        if db.execute("SELECT username FROM users WHERE username = ?", user):
            return apology("This username is taken Try again", 400)

        psw = generate_password_hash(psw)
        register = db.execute("INSERT INTO users (username, hash) VALUES(?,?)", user, psw)
        session["user_id"] = register

        return redirect("/")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        id = session["user_id"]
        data = db.execute("SELECT symbol,SUM(shares) as share FROM ledger WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", id)
        return render_template("sell.html", datas=data)
    else:
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        if shares < 1:
            return apology("Please Enter a Positive number", 403)

        if not symbol:
            return apology("Please Enter a symbol", 403)

        if not shares:
            return apology("Please Enter number of shares", 403)

        stock = lookup(symbol)
        if not stock:
            return apology("Please Enter a Valid Symbol", 403)

        price = stock["price"]
        cost = price * int(shares)

        id = session["user_id"]
        balance = db.execute("SELECT cash FROM users WHERE id = ?", id)[0]
        id = session["user_id"]
        current_shares = db.execute("SELECT SUM(shares) as st FROM ledger WHERE symbol = ? AND user_id = ?", symbol, id)
        print(current_shares)
        owned = current_shares[0]["st"]
        if shares > owned:
            return apology("Not Enough Shares", 400)

        new_cash = balance["cash"] + cost
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, id)
        time = datetime.now()
        db.execute("INSERT INTO ledger (user_id, symbol, name, shares, price, date) VALUES(? ,? ,? ,? ,?, ? )",
                   session["user_id"], stock["symbol"], stock["name"], (-1)*shares, stock["price"], time)
        flash("SOLD!")
        return redirect("/")
