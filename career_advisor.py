import streamlit as st
import pandas as pd

# --------------------------
# 🎓 University Database (Islamabad, 2026 Official Prospectus Data)
# --------------------------
uni_data = pd.DataFrame([
    {
        "University": "NUST",
        "Programs": "BS Computer Science, BS Artificial Intelligence, BS Software Engineering, BS Electrical Engineering, BBA",
        "Eligibility": "Matric ≥60%, FSc/ICS/A‑Levels ≥60%, Clear NET Entry Test",
        "Merit Range": "85% – 92%",
        "Fees Per Semester": "PKR 190,000 – 260,000",
        "Admission Period": "May – June",
        "Deadline": "Mid July",
        "Career Scope": "Top jobs in tech, government, multinational firms; starting salary ~70,000 – 150,000+",
        "HEC Recognized": "✅ Yes"
    },
    {
        "University": "COMSATS University Islamabad",
        "Programs": "BS CS, BS AI, BS SE, BS Cyber Security, BBA, BS Accounting & Finance",
        "Eligibility": "Matric ≥50%, FSc/ICS ≥50%, Entry Test or NTS",
        "Merit Range": "75% – 88%",
        "Fees Per Semester": "PKR 90,000 – 130,000",
        "Admission Period": "June – July",
        "Deadline": "End August",
        "Career Scope": "Strong industry demand; starting salary ~50,000 – 120,000",
        "HEC Recognized": "✅ Yes"
    },
    {
        "University": "FAST‑NUCES Islamabad",
        "Programs": "BS Computer Science, BS Artificial Intelligence, BS Software Engineering",
        "Eligibility": "Matric ≥60%, FSc/ICS ≥60%, FAST Entry Test",
        "Merit Range": "82% – 90%",
        "Fees Per Semester": "PKR 150,000 – 190,000",
        "Admission Period": "May – July",
        "Deadline": "Mid July",
        "Career Scope": "Best for software industry; starting salary ~80,000 – 180,000+",
        "HEC Recognized": "✅ Yes"
    },
    {
        "University": "International Islamic University (IIUI)",
        "Programs": "BS CS, BS SE, BBA, BS Electrical Engineering, BS Psychology, BS Mass Communication",
        "Eligibility": "Matric ≥50%, FSc/ICS/Commerce ≥50%, No entry test for most programs",
        "Merit Range": "60% – 75%",
        "Fees Per Semester": "PKR 40,000 – 70,000",
        "Admission Period": "June – July",
        "Deadline": "End August",
        "Career Scope": "Good public & private sector jobs; very affordable",
        "HEC Recognized": "✅ Yes"
    },
    {
        "University": "NUTECH Islamabad",
        "Programs": "BS CS, BS AI, BS Mechanical Engineering, BS Civil Engineering",
        "Eligibility": "Matric ≥60%, FSc ≥50%, NUTECH Entry Test",
        "Merit Range": "70% – 82%",
        "Fees Per Semester": "PKR 80,000 – 110,000",
        "Admission Period": "June – July",
        "Deadline": "End August",
        "Career Scope": "Growing demand in engineering & tech sector",
        "HEC Recognized": "✅ Yes"
    },
    {
        "University": "Air University Islamabad",
        "Programs": "BS CS, BS SE, BS Electrical Engineering, BBA",
        "Eligibility": "Matric ≥60%, FSc ≥60%, Entry Test",
        "Merit Range": "78% – 86%",
        "Fees Per Semester": "PKR 110,000 – 150,000",
        "Admission Period": "June – July",
        "Deadline": "Early August",
        "Career Scope": "Good reputation, jobs in aviation & IT",
        "HEC Recognized": "✅ Yes"
    }
])

# --------------------------
# 🎨 App Interface
# --------------------------
st.set_page_config(page_title="AI Career Advisor | Pakistan", layout="wide")
st.title("🎓 AI Career Advisor — For Pakistani Students")
st.write("Get personalized guidance: which university, program, fees, deadlines and career path fits you best.")

# User Inputs
col1, col2, col3 = st.columns(3)
marks = col1.number_input("Your Intermediate / A‑Level Percentage", min_value=33, max_value=100, value=60)
stream = col2.selectbox("Your Study Stream", ["FSc Pre‑Engineering", "FSc Pre‑Medical", "ICS / Computer Science", "Commerce", "Arts / Humanities"])
budget = col3.number_input("Maximum Budget per Semester (PKR, thousands)", min_value=20, max_value=300, value=120)

# --------------------------
# 🔍 Matching Logic
# --------------------------
if st.button("🔎 Get My Career Plan"):
    def get_min_eligibility(text):
        try:
            return int(text.split("≥")[1].split("%")[0])
        except:
            return 50

    def get_max_fee(text):
        try:
            return int(text.split("–")[1].strip().replace(",", "").split(" ")[0])
        except:
            return 300

    uni_data["Min Eligibility"] = uni_data["Eligibility"].apply(get_min_eligibility)
    uni_data["Max Fee"] = uni_data["Fees Per Semester"].apply(lambda x: get_max_fee(x.replace("PKR ", "")))

    results = uni_data[
        (marks >= uni_data["Min Eligibility"]) &
        (budget * 1000 >= uni_data["Max Fee"])
    ].drop(columns=["Min Eligibility", "Max Fee"])

    if not results.empty:
        st.success(f"✅ Found {len(results)} matching universities/programs:")
        st.dataframe(results, use_container_width=True)
        st.info("📌 Next Steps: Visit the official university website, check test dates, and apply before the deadline!")
    else:
        st.warning("⚠️ No matching options found. Try adjusting your marks or budget.")

st.info("ℹ️ Data source: Official university prospectuses & admission portals (2026). All universities are HEC‑recognized.")
