from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/drivers_license")
def drivers_license():
    
    documents = [
        "Aadhar Card (Identity Proof)",
        "Address Proof (Electricity Bill / Ration Card)",
        "Birth Certificate or 10th Marksheet",
        "Passport Size Photos",
        "Learner's License"
    ]
    
    steps = [
        "Apply online through Parivahan website",
        "Book a driving test slot",
        "Visit the RTO office",
        "Give driving test",
        "Receive Driving License by post"
    ]
    
    estimated_cost = "₹500 - ₹1500 (varies by state)"
    
    return render_template(
        "drivers_license.html",
        docs=documents,
        process_steps=steps,
        cost=estimated_cost
    )


@app.route("/voters_id")
def voters_id():
    
    documents = [
        "Aadhar Card (Identity Proof)",
        "Address Proof",
        "Passport Size Photograph",
        "Mobile Number",
        "Age Proof (Birth Certificate / 10th Marksheet)"
    ]
    
    steps = [
        "Visit the National Voters' Service Portal",
        "Fill Form 6 for new voter registration",
        "Upload required documents",
        "Submit the application",
        "Wait for verification",
        "Receive Voter ID card by post"
    ]
    
    estimated_cost = "Free of cost"
    
    return render_template(
        "voters_id.html",
        docs=documents,
        process_steps=steps,
        cost=estimated_cost
    )

@app.route("/passport")
def passport():
    
    passport_data = {
        "Adult": {
            "documents": [
                "Aadhar Card",
                "PAN Card",
                "Address Proof",
                "Birth Certificate"
            ],
            "cost": "₹1500 (Normal) / ₹3500 (Tatkal)"
        },
        
        "Minor": {
            "documents": [
                "Birth Certificate",
                "Parents' Passport Copy",
                "Address Proof of Parents",
                "Passport Size Photos"
            ],
            "cost": "₹1000"
        },
        
        "Senior Citizen": {
            "documents": [
                "Aadhar Card",
                "Age Proof",
                "Address Proof",
                "Old Passport (if renewal)"
            ],
            "cost": "₹1500"
        }
    }

    return render_template("passport.html", passport_data=passport_data)


if __name__ == "__main__":
    app.run(debug=True)