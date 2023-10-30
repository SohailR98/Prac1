from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Connect to the database
conn = sqlite3.connect('inventory.db')
c = conn.cursor()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quote', methods=['POST'])
def quote():
    # Get client information
    client_name = request.form['client_name']
    client_phone = request.form['client_phone']
    site_location = request.form['site_location']

    # Initialize variables
    total_price = 0
    room_prices = []

    # Get room information
    room_names = request.form.getlist('room_name')
    for room_name in room_names:
        devices = []
        device_names = request.form.getlist(f'{room_name}_device_name')
        device_quantities = request.form.getlist(
            f'{room_name}_device_quantity')
        for device_name, device_quantity in zip(device_names, device_quantities):
            # Query the database for the device price
            c.execute("SELECT price FROM products WHERE name=?", (device_name,))
            device_price = c.fetchone()[0]
            # Calculate the device price
            device_total_price = device_price * int(device_quantity)
            # Add the device to the list
            devices.append((device_name, device_quantity, device_total_price))
            # Add the device price to the total price
            total_price += device_total_price
        # Add the room to the list
        room_prices.append((room_name, devices))

    # Add additional charges if the site location is far
    if site_location == 'far':
        total_price *= 1.1

    # Add profit margin
    total_price *= 1.2

    # Close the database connection
    conn.close()

    # Save the quotation to the database
    conn = sqlite3.connect('quotations.db')
    c = conn.cursor()
    c.execute("INSERT INTO quotations (client_name, client_phone, site_location, room_prices, total_price) VALUES (?, ?, ?, ?, ?)",
              (client_name, client_phone, site_location, str(room_prices), total_price))
    conn.commit()
    conn.close()

    return render_template('quote.html', room_prices=room_prices, total_price=total_price)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
