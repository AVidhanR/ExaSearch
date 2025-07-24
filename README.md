## ExaSearch WebApp
- I've developed a user-friendly web application utilizing Streamlit, designed to facilitate seamless content searches on Wikipedia. Leveraging the exa-api, users can access Wikipedia's vast repository of information directly through the app. Whether you're a student, researcher, or simply curious, this tool offers a convenient way to explore and discover knowledge.

- I used `exa_py` and `streamlit` packages in this project.

```txt
Directory structure:
└── avidhanr-exasearch/
    ├── README.md
    ├── requirements.txt
    └── app/
        ├── navigation.py
        └── pages/
            ├── about.py
            ├── exa_search.py
            └── footer.py
```

- Get the `Exa API KEY` from [`here`](https://dashboard.exa.ai/api-keys)

- Checkout the cheatsheet to get a basic understanding of how to use `Exa API` from [`here`](https://docs.exa.ai/reference/cheat-sheet)

- Checkout the official `StreamLit` documentation from [`here`](https://docs.streamlit.io/get-started)

## How to run this project?

- Open the integrated terminal and run the following command to install the required packages:

```bash
pip install -r requirements.txt
```

- The `requirements.txt` file contains the list of packages used in this project.
- After installing the required packages, run the following command to start the Streamlit app:

```bash
streamlit run app/navigation.py
```

- The Streamlit app will open in the default web browser.
- The app contains the following pages:

  - Home (Exa Search)
  - About

- Visit the web app from [`here`](https://exa-search-web.streamlit.app/)
- Fork this `repo` and experiment on it.
- Project by [`AVidhanR`](https://linktr.ee/itsvidhanreddy)
