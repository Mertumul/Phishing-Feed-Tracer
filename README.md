# Phishing Feed Monitoring Project

## Project Overview

This project aims to monitor phishing feeds and store this data in a database to protect against phishing attacks. The project includes technologies that will be used to extract data from platforms known for hosting phishing content. By continuously tracking and storing this data, we enhance cybersecurity measures.

Additionally, the collected phishing feed data can be accessed through a FastAPI-based API, providing users with real-time information on phishing threats. This proactive approach allows organizations to stay ahead of potential risks and take immediate action when needed.

## Table of Contents

- [Objectives](#objectives)
- [Technologies Used](#technologies-used)
- [Phishing Resources](#phishing-resources)
- [Guidelines](#guidelines)
- [Getting Started](#getting-started)


## Objectives

- Develop a robust system for tracking and monitoring phishing feeds.
- Extract and collect relevant data from identified sources and platforms.
- Store the gathered data securely in a database for further analysis.
- Implement safeguards to enhance protection against phishing attacks.
- Expose the collected phishing feed data through a FastAPI-based API.

## Technologies Used

To accomplish the objectives of this project, we leverage the following technologies:

- [Poetry](https://python-poetry.org/docs/): A powerful tool for managing dependencies and packaging.
- Docker Compose: Facilitates the creation and operation of multi-container Docker applications.
- [FastAPI](https://fastapi.tiangolo.com/tr/): A modern and fast web framework for building APIs with Python 3.7+.
- [ORM (Object-Relational Mapping)](https://docs.sqlalchemy.org/en/20/orm/): A versatile tool for interacting with databases.
- PostgreSQL: An open-source relational database management system.

## Phishing Resources

The following phishing resources are used in this project to monitor and extract data:

- [USOM Phishing Feed](https://www.usom.gov.tr/url-list.txt): A feed provided by USOM.
- [URLhaus Phishing Feed](https://urlhaus.abuse.ch/downloads/text_online/): A feed from URLhaus.
- [AlienVault Vetted Phishing Feed](https://otx.alienvault.com/otxapi/pulses/60a794fa6de6293139323f21/indicators/?sort=-created&limit=10000&page=1): Vetted phishing indicators from AlienVault.
- [AlienVault Turkey Phishing Feed](https://otx.alienvault.com/otxapi/pulses/64b13f10dd3a7cdbcecd89b7/indicators/?sort=-created&limit=1000&page=1): Turkish-specific phishing indicators from AlienVault.
- [AlienVault Domain Phishing Feed](https://otx.alienvault.com/otxapi/pulses/64b13f10dd3a7cdbcecd89b7/indicators/?sort=-created&limit=1000&page=1): Domain-related phishing indicators from AlienVault.
- [AlienVault URL Phishing Feed](https://otx.alienvault.com/otxapi/pulses/5e98271289d56c79998870d9/indicators/?sort=-created&limit=10000&page=1): URL-related phishing indicators from AlienVault.
- [Tweet Feed](https://raw.githubusercontent.com/0xDanielLopez/TweetFeed/master/year.csv): A feed of phishing-related tweets.
- [Phishtank Feed](https://data.phishtank.com/data/online-valid.csv): An online-valid phishing feed from Phishtank.



## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using Poetry.
3. Set up the project configuration, including database connections.
4. Run the FastAPI server to start monitoring phishing feeds.

Detailed instructions and examples can be found in the project documentation.


