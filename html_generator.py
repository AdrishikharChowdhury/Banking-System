def generateBankStatement(self,file):
    file.write(f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bank Statement {self.acc_no}</title>
        <link rel="stylesheet" href="./assets/style.css">
        <link rel="stylesheet" href="./assets/mobile.css">
    </head>
    <body>
        <div class="info">
            <p>Bank Statement</p>
            <ul class="holder-info">
                <li>Name:           <div class="data">{self.name}</div></li>
                <li>Email:          <div class="data">{self.email}</div></li>
                <li>Contact:        <div class="data">{self.contact}</div></li>
                <li>Account Type:   <div class="data">{self.type}</div></li>
                <li>Account Number: <div class="data">{self.acc_no}</div></li>
                <li>Balance:        <div class="data">{self.acc_bal}</div></li>
                <li>Unique ID:      <div class="data">{self.uid}</div></li>
            </ul>
        </div>
        <table class="statement">
            <thead>
                <tr class="heading-statement">
                    <th>Date and Time</th>
                    <th>Type</th>
                    <th>Amount</th>
                    <th>Balance</th>
                    <th>Transaction ID</th>
                </tr>
            </thead>
            <tbody>""")

    if not self.transactions:
        file.write("""
        <tr class="data-statement">
            <td colspan="5" style="text-align: center;">No Transaction History</td>
        </tr>""")
    else:
        for txn in self.transactions:
            file.write(f"""
        <tr class="data-statement">
            <td>{txn.datetime}</td>
            <td>{txn.type}</td>
            <td>{txn.amount}</td>
            <td>{txn.balance}</td>
            <td>{txn.transactionId}</td>
        </tr>""")

    file.write(f"""
    </tbody>
</table>
        <div class="final">
            <p>Final Balance: ₹{self.acc_bal}</p>
        </div>
    </body>
    </html>""")