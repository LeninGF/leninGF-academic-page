from flask import Flask, render_template

app = Flask(__name__)

# ── Data ──────────────────────────────────────────────────────────────────────

PROFILE = {
    "name": "Lenin Gonzalo Falconi Estrada",
    "name_short": "Lenin G. Falconi",
    "affiliation": "Escuela Politécnica Nacional",
    "department": "Department of Informatics and Computer Sciences",
    "location": "Quito, Ecuador",
    "email": "lenin.falconi@epn.edu.ec",
    "orcid": "0000-0003-4402-6643",
    "github": "LeninGF",
    "scholar": "https://scholar.google.com/citations?user=4Xk02pkAAAAJ&hl=en&oi=ao",
    "linkedin": "https://www.linkedin.com/in/lenin-g-falconi",
    "researchgate": "https://www.researchgate.net/profile/Lenin-Falconi",
    "bio_paragraphs": [
        (
            "I earned my Electronic Engineering degree in Automation from "
            "Escuela Politécnica Nacional (EPN) in 2013 and my Master's in "
            "Computer Science in 2020. I am currently pursuing a PhD in "
            "Computer Science at the same institution."
        ),
        (
            "From 2019 to 2021, I served as a research assistant at the "
            "Computer Science and Informatics Department. From 2021 to 2024, "
            "I worked at the Fiscalía General del Estado, where I developed "
            "a large language model for classifying robbery categories from text."
        ),
        (
            "Currently I am a part-time professor at the Department of "
            "Informatics and Computer Sciences at EPN. My research focuses on "
            "Machine Learning, Computer Vision, and Natural Language Processing."
        ),
    ],
}

EDUCATION = [
    {
        "degree": "PhD in Computer Science",
        "school": "Escuela Politécnica Nacional",
        "period": "2021 – Present",
        "note": "Focus: Medical imaging and deep learning for breast cancer diagnosis.",
    },
    {
        "degree": "MSc in Computer Science",
        "school": "Escuela Politécnica Nacional",
        "period": "2018 – 2020",
    },
    {
        "degree": "Electronic Engineering (Automation)",
        "school": "Escuela Politécnica Nacional",
        "period": "2007 – 2013",
    },
]

EXPERIENCE = [
    {
        "role": "Part-time Professor",
        "place": "Dept. of Informatics and Computer Sciences, EPN",
        "period": "2024 – Present",
    },
    {
        "role": "Developer / NLP Researcher",
        "place": "Fiscalía General del Estado, Ecuador",
        "period": "2021 – 2024",
        "desc": (
            "Developed a large language model for classifying robbery "
            "categories from text."
        ),
    },
    {
        "role": "Research Assistant",
        "place": "Computer Science and Informatics Dept., EPN",
        "period": "2019 – 2021",
    },
]

RESEARCH_INTERESTS = [
    {
        "title": "Medical Image Segmentation",
        "description": (
            "Developing deep-learning based segmentation models for "
            "thermogram and mammogram images to assist in breast cancer "
            "detection and diagnosis."
        ),
    },
    {
        "title": "Deep Learning & Transfer Learning",
        "description": (
            "Applying and fine-tuning pre-trained convolutional neural "
            "networks (MobileNet, NASNet) for medical image classification "
            "tasks on limited datasets."
        ),
    },
    {
        "title": "Natural Language Processing",
        "description": (
            "Building large language models for legal text classification "
            "and analysis at the Fiscalía General del Estado."
        ),
    },
]

PUBLICATIONS = [
    {
        "title": (
            "Transfer Learning and Fine Tuning in Breast Mammogram "
            "Abnormalities Classification on CBIS-DDSM Database"
        ),
        "authors": "Lenin G. Falconi, María Pérez, Wilbert G. Aguilar",
        "venue": "Advances in Science, Technology and Engineering Systems Journal (ASTESJ)",
        "volume": "Vol. 5, No. 2, pp. 154–159",
        "year": "2020",
        "doi": "10.25046/aj050220",
        "type": "journal",
    },
    {
        "title": (
            "Transfer Learning and Fine Tuning in Mammogram BI-RADS "
            "Classification"
        ),
        "authors": "Lenin G. Falconi, María Pérez, Wilbert G. Aguilar",
        "venue": "2020 IEEE 33rd International Symposium on Computer-Based Medical Systems (CBMS)",
        "volume": "",
        "year": "2020",
        "doi": "10.1109/CBMS49503.2020.00096",
        "type": "conference",
    },
    {
        "title": (
            "Transfer Learning in Breast Mammogram Abnormalities "
            "Classification with MobileNet and NASNet"
        ),
        "authors": "Lenin G. Falconi, María Pérez, Wilbert G. Aguilar",
        "venue": "2019 International Conference on Systems, Signals and Image Processing (IWSSIP)",
        "volume": "",
        "year": "2019",
        "doi": "10.1109/IWSSIP.2019.8787295",
        "type": "conference",
    },
]

# ── Routes ────────────────────────────────────────────────────────────────────


@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        publications=PUBLICATIONS,
        interests=RESEARCH_INTERESTS,
        education=EDUCATION,
        experience=EXPERIENCE,
        active="home",
    )


@app.route("/publications")
def publications():
    return render_template(
        "publications.html",
        profile=PROFILE,
        publications=PUBLICATIONS,
        interests=RESEARCH_INTERESTS,
        education=EDUCATION,
        experience=EXPERIENCE,
        active="publications",
    )


@app.route("/research")
def research():
    return render_template(
        "research.html",
        profile=PROFILE,
        publications=PUBLICATIONS,
        interests=RESEARCH_INTERESTS,
        education=EDUCATION,
        experience=EXPERIENCE,
        active="research",
    )


@app.route("/cv")
def cv():
    return render_template(
        "cv.html",
        profile=PROFILE,
        publications=PUBLICATIONS,
        interests=RESEARCH_INTERESTS,
        education=EDUCATION,
        experience=EXPERIENCE,
        active="cv",
    )


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
