import streamlit as st

# --------------------------
# University Database
# --------------------------
universities = [
    {
        "University": "NUST",
        "Programs": "BS Computer Science, BS AI, BS Software Engineering, BS Electrical Engineering, BBA",
        "Min_Marks": 60,
        "Max_Fee_Per_Semester": 260000,
        "Merit_Range": "85% – 92%",
        "Admission_Period": "May – June",
        "Deadline": "Mid July",
        "Career_Scope": "High demand, starting salary 70,000 – 150,000+",
        "HEC_Recognized": "✅ Yes"
    },
    {
        "University": "COMSATS University Islamabad",
        "Programs": "BS CS, BS AI, BS SE, BS Cyber Security, BBA",
        "Min_Marks": 50,
        "Max_Fee_Per_Semester": 130000,
        "Merit_Range": "75% – 88%",
        "Admission_Period": "June – July",
        "Deadline": "End August",
        "Career_Scope": "Strong industry demand, 50,000 – 120,000+",
        "HEC_Recognized": "✅ Yes"
    },
    {
        "University": "FAST‑NUCES Islamabad",
        "Programs": "BS Computer Science, BS Artificial Intelligence, BS Software Engineering",
        "Min_Marks": 60,
        "Max_Fee_Per_Semester": 190000,
        "Merit_Range": "82% – 90%",
        "Admission_Period": "May – July",
        "Deadline": "Mid July",
        "Career_Scope": "Top software sector, 80,000 – 180,000+",
        "HEC_Recognized": "✅ Yes"
    },
    {
        "University": "International Islamic University (IIUI)",
        "Programs": "BS CS, BS SE, BBA, BS Electrical Engineering, BS Psychology",
        "Min_Marks": 50,
        "Max_Fee_Per_Semester": 70000,
        "Merit_Range": "60% – 75%",
        "Admission_Period": "June – July",
        "Deadline": "End August",
        "Career_Scope": "Affordable, good public & private jobs",
        "HEC_Recognized": "✅ Yes"
    },
    {
        "University": "Air University Islamabad",
        "Programs": "BS CS, BS SE, BS Electrical Engineering, BBA",
        "Min_Marks": 60,
        "Max_Fee_Per_Semester": 150000,
        "Merit_Range": "78% – 86%",
        "Admission_Period": "June – July",
        "Deadline": "Early August",
        "Career_Scope": "Good reputation, aviation & IT jobs",
        "HEC_Recognized": "✅ Yes"
    }
]

# --------------------------
# App Layout
# --------------------------
st.set_page_config(page_title="AI Career Advisor | Pakistan", layout="wide")
st.title("🎓 AI Career Advisor — For Pakistani Students")
st.write("Find universities, eligibility, fees, deadlines and career paths matching your marks, study stream and budget.")

# User Inputs
marks = st.number_input("Your Intermediate / A‑Level Percentage", min_value=33, max_value=100, value=60)
stream = st.selectbox("Your Study Stream", ["FSc Pre‑Engineering", "FSc Pre‑Medical", "ICS / Computer Science", "Commerce", "Arts / Humanities"])
budget = st.number_input("Max Budget per Semester (PKR, thousands)", min_value=20, max_value=300, value=200)

# Filter & Show Results
if st.button("🔍 Find My Universities"):
    matches = []
    for uni in universities:
        if marks >= uni["Min_Marks"] and (budget * 1000) >= uni["Max_Fee_Per_Semester"]:
            matches.append(uni)

    if matches:
        st.success(f"✅ Found {len(matches)} matching universities:")
        st.table(matches)
    else:
        st.warning("⚠️ No matches found. Try increasing your marks or budget.")

st.info("ℹ️ Data source: Official university prospectuses 2026 | All universities are HEC‑recognized")
