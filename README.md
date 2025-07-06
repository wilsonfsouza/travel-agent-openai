<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/wilsonfsouza/travel-agent-openai">

   <img alt="License" src="https://img.shields.io/badge/license-MIT-%23F26C6C">


  <a href="https://www.linkedin.com/in/wilsonfsouza/">
    <img alt="Made by Wilson Franca" src="https://img.shields.io/badge/made%20by-Wilson%20Franca-%230AA186">
  </a>
</p>

<h1 align="center">
  Travel Agent LLM (OpenAI)
</h1>

<h4 align="center">
  Table of contents
</h4>

<p align="center">
 <a href="#-about-the-project">About</a> •
 <a href="#-features">Features</a> • 
 <a href="#-technologies">Technologies</a> •
 <a href="#-author">Author</a> •
 <a href="#user-content--license">License</a>
</p>


## 💻 About the project

Project using OpenAI to simulate a travel agency with a supervisor and workers LLMs that can access the internet to retrieve a travel itinerary for an England trip.

> OBS: I initially had this deployed in an AWS lambda (see [lambda_handler](https://github.com/wilsonfsouza/travel-agent-openai/blob/main/travelAgent.py) function); however, I took it down since it was charging my credit card for $20/monthly.

---

## ⚙️ Features

The workers will leverage Beuatiful Soup to web scrap relevant information on:
- [Wikipedia](http://en.wikipedia.org/wiki/Main_Page)
- [Travel Tips](https://www.dicasdeviagem.com/inglaterra/)

The supervisor will review the work done by the workers and return a travel itinerary with a list of events happening in the week of the trip, flight tickets pricing, and additional requests made by the user.

---

## 🛠 Technologies

The following tools were used in this project:

-   **[Python](https://www.python.org/)**
-   **[OpenAI](https://openai.com/)**
-   **[LangChain](https://www.langchain.com/)**
-   **[Beautiful Soup 4 (bs4)](https://beautiful-soup-4.readthedocs.io/en/latest/)**
-   **[dotenv](https://pypi.org/project/python-dotenv/)**

> See the file  [requirements.txt](https://github.com/wilsonfsouza/travel-agent-openai/blob/main/requirements.txt)

---

## 💪 How to contribute to this project

1. **Fork** the project.
2. Start a new branch with your changes: `git checkout -b my-new-feature`
3. Save it and create a commit message describing what you have done: `git commit -m "feature: My new feature"`
4. Send your alterations: `git push origin my-feature`


---

## 👨‍💻 Author

<br/>
<h3>
 <img style="border-radius: 50%; margin-right: 20px; width: 80px;" src="https://avatars0.githubusercontent.com/u/21347383?s=460&u=fdb399c92e369762d45d6495cbd2e87eef9e4d65&v=4" width="100px;" alt=""/>
 <br />
 <sub>Wilson Franca</sub></h3>
 <br />

[![Linkedin Badge](https://img.shields.io/badge/-Wilson-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/wilsonfsouza/)](https://www.linkedin.com/in/wilsonfsouza/)
[![Gmail Badge](https://img.shields.io/badge/-wilson.franca.92@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:wilson.franca.92@gmail.com)](mailto:wilson.franca.92@gmail.com)

---

## 📝 License

This project is being developed under [MIT License](./LICENSE).

Made with ❤️ by Wilson Franca 👋

