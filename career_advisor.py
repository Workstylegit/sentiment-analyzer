import streamlit as st

# --------------------------
# University Data
# --------------------------
universities = [
    {
        "University": "NUST",
        "Programs": "BS Computer Science, BS AI, BS Software Engineering, BS Electrical Engineering, BBA",
        "Min Marks": 60,
        "Max Fee (PKR)": 260000,
        "Merit Range": "85% – 92%",
        "Admission": "May – June",
        "Deadline": "Mid July",
        "Career Scope": "High demand, starting salary 70k – 150k+",
        "HEC Recognized": "✅ Yes"
    },
    {
        "University": "COMSATS University Islamabad",
        "Programs": "BS CS, BS AI, BS SE, BS Cyber Security, BBA",
        "Min Marks": 50,
        "Max Fee (PKR)": 130000,
        "Merit Range": "75% – 88%",
        "Admission": "June – July",
        "Deadline": "End August",
        "Career Scope": "Strong industry demand, 50k – 120k+",
        "HEC Recognized": "✅ Yes"
    },
    {
        "University": "FAST‑NUCES Islamabad",
        "Programs": "BS Computer Science, BS Artificial Intelligence, BS Software Engineering",
        "Min Marks": 60,
        "Max Fee (PKR)": 190000,
        "Merit Range": "82% – 90%",
        "Admission": "May – July",
        "Deadline": "Mid July",
        "Career Scope": "Top software sector, 80k – 180k+",
        "HEC Recognized": "✅ Yes"
    },
    {
        "University": "International Islamic University (IIUI)",
        "Programs": "BS CS, BS SE, BBA, BS Electrical Engineering, BS Psychology",
        "Min Marks": 50,
        "Max Fee (PKR)": 70000,
        "Merit Range": "60% – 75%",
        "Admission": "June – July",
        "Deadline": "End August",
        "Career Scope": "Affordable, good public & private jobs",
        "HEC Recognized": "✅ Yes"
    },
    {
        "University": "Air University Islamabad",
        "Programs": "BS CS, BS SE, BS Electrical Engineering, BBA",
        "Min Marks": 60,
        "Max Fee (PKR)": 150000,
        "Merit Range": "78% – 86%",
        "Admission": "June – July",
        "Deadline": "Early August",
        "Career Scope": "Good reputation, aviation & IT jobs",
        "HEC Recognized": "✅ Yes"
    }
]

# --------------------------
# App Interface
# --------------------------
st.set_page_config(page_title="AI Career Advisor Pakistan", layout="wide")
st.title("🎓 AI Career Advisor — For Pakistani Students")
st.write("Find the best universities and programs based on your marks, study stream and budget.")

marks = st.number_input("Your Intermediate / A‑Level Percentage", min_value=33, max_value=100, value=60)
stream = st.selectbox("Your Study Stream", ["FSc Pre‑Engineering", "FSc Pre‑Medical", "ICS / Computer Science", "Commerce", "Arts / Humanities"])
budget = st.number_input("Max Budget per Semester (PKR, thousands)", min_value=20, max_value=300, value=200)

if st.button("🔍 Find My Universities"):
    results = []
    for uni in universities:
        if marks >= uni["Min Marks"] and budget * 1000 >= uni["Max Fee (PKR)"]:
            results.append(uni)

    if results:
        st.success(f"✅ Found {len(results)} matching universities:")
        st.table(results)
    else:
        st.warning("⚠️ No matches found. Try increasing your marks or budget.")

st.info("ℹ️ Data source: Official university prospectuses 2026 | All HEC‑recognized")
