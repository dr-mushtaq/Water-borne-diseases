# 🏥 Hospital-Connected Disease Surveillance and Early-Warning Platform

## 🎯 Overview

The **Hospital-Connected Disease Surveillance and Early-Warning Platform** is a proposed AI-powered public health system designed to connect **hospitals, diagnostic laboratories, and district health departments**.

Hospitals will **upload patient and laboratory records or automatically synchronize data** through approved integrations. The platform will use **Machine Learning (ML), geographic analysis, and surveillance rules** to monitor **malaria and typhoid**, forecast case trends, identify potential hotspots, and generate alerts for **district health officers**.

The platform aims to help health teams identify unusual increases in reported cases, investigate affected areas, and prioritize response resources.

> **Project status:** Research and planning stage. The features below describe the intended product; a runnable application and validated prediction models are not yet available in this workspace.

⚠️ **Disclaimer:** This project is currently for **educational, research, and prototyping purposes**. Predictions and alerts require evaluation and authorized professional review before operational use. The platform does not provide prescriptions or replace clinical diagnosis or laboratory confirmation.

**Disease scope:** Malaria is primarily mosquito-borne, so the platform uses the broader term **disease surveillance** rather than describing both diseases as waterborne. [WHO malaria fact sheet](https://www.who.int/news-room/fact-sheets/detail/malaria).

---

## 🤝 Contributing

We welcome suggestions and contributions to this list of Water-borne diseases!

### ✅ How to Contribute

1. **Fork** this repository.
2. **Add your Projects Folder** in the appropriate category (alphabetically, if possible).
3. Include the following details:
   - Folder Name **Student Name** (Student ID)- include following files
     - A **Details description of your project.md file **
     - Complete Code
     - Complete Diagram
4. Create a **Pull Request (PR) after Final Viva** with a clear title and description of your changes.
5.  Please read:[CONTRIBUTING.md](https://github.com/dr-mushtaq/Water-borne-diseases/blob/main/CONTRIBUTING.md)

---

### 💡 Alternative: Suggest via GitHub Issues

If you're not familiar with Git or Pull Requests, you can still contribute:

- Open a **GitHub Issue** with the following format:
- Sent email : mushtaq.hussain@vu.edu.pk

---
<details>
<summary>

## 🎯 Objectives

- Enable **hospital and laboratory data uploads and automated synchronization**.
- Monitor **suspected and confirmed malaria and typhoid cases** separately.
- Develop **area-level disease risk estimates and case forecasts**.
- Identify **geographic hotspots and unusual increases in reported cases**.
- Generate **early-warning alerts for district health officers**.
- Provide **interactive dashboards and aggregate surveillance reports**.
- Support a **mobile-friendly web interface and approved API integrations**.
- Build a **scalable, modular platform with controlled data access**.

---

## ✅ Quick Start Checklist with Links

- Review the [Research Foundation](#-research-foundation).
- Explore the [System Architecture](#-system-architecture).
- View the [Dashboard Reference](#-dashboard-reference).
- Define the [Data Requirements](#-data-requirements) with participating hospitals.
- Follow the [Development Plan](#-development-plan).
- Related work Review Sheet [Related work Review Sheet](https://docs.google.com/spreadsheets/d/17c9r8ydv93V2gInOBzJR9l85RrYYYptdluYYziDOTv8/edit?usp=sharing).
- Agree on case definitions, reporting frequency, alert ownership, and authorized data use.
- Prepare synthetic data for the initial prototype.

**Setup status:** Installation commands will be added when application code and dependencies are available. This workspace currently contains documentation, the reference paper, and the dashboard image.

## 🏗️ System Architecture


### 1. Disease Surveillance and Analytics Engine

- Collect and validate disease and laboratory records from participating facilities
- Analyze suspected and confirmed cases by disease, location, and reporting period
- Compare recent case counts with historical or seasonal baselines
- Explore forecasting and hotspot-detection approaches
- Generate signals for review by authorized public health personnel

### 2. Hospital and Laboratory Reporting

- Accept standardized data through CSV uploads
- Support future integration with approved hospital and laboratory systems
- Validate required fields, dates, disease classifications, and test results
- Identify duplicate submissions and track corrections
- Report missing or delayed facility submissions

### 2. AI and Early-Warning Engine

- Aggregate case records by disease, geographic area, and reporting period.
- Compare current observations with historical and seasonal baselines.
- Evaluate candidate models for **future case counts and area-level risk**.
- Display forecast horizons and uncertainty intervals.
- Generate alerts when approved surveillance thresholds are exceeded.
- Record model versions, triggering rules, and supporting evidence.

### 3. Surveillance Dashboard

- Provide disease filters for **malaria and typhoid**.
- Display case summaries, time trends, geographic patterns, and active alerts.
- Show reporting coverage and the latest data refresh time.
- Offer separate views for hospital staff and district health officers.
- Support acknowledgment, investigation notes, assignment, and alert closure.
- Display case summaries, trends, geographic patterns, and alerts
- Provide separate views for malaria and typhoid
- Show reporting coverage and the latest data update
- Help health teams review and investigate unusual changes

### 4. Data and Analytics Layer

- Store validated records with source and import history.
- Maintain aggregate surveillance datasets and geographic boundaries.
- Store forecasts, alert history, and audit records.
- Apply role-based access and organization boundaries.
- Support authorized aggregate reporting and reproducible model evaluation.

```mermaid
flowchart TD
    A[Hospitals and Laboratories] --> B[CSV Uploads or Approved API Sync]
    B --> C[Validation and Deduplication]
    C --> D[Restricted Data Storage]
    C --> E[Errors Returned for Correction]
    D --> F[Aggregation and Analytics]
    F --> G[Surveillance Rules and Forecast Models]
    G --> H[Dashboard and Hotspot Maps]
    G --> I[Alert Queue]
    I --> J[District Health Officer Review]
    J --> K[Investigation and Resolution]
```

## 📌 Key Features

### 🦠 Disease Surveillance

- Monitor malaria and typhoid cases separately
- Distinguish suspected cases from confirmed cases
- Review disease trends across reporting periods and locations
- Keep observed data separate from forecasts or model estimates

### 🏥 Hospital and Laboratory Reporting

- Plan for standardized data uploads
- Validate incoming records and provide error summaries
- Track reporting completeness and data freshness
- Support future connections to approved health information systems

### 🗺️ Geographic Monitoring

- Summarize reported cases by approved district or locality boundaries
- Highlight unusual increases for further investigation
- Distinguish a patient's area of residence from the reporting facility
- Consider missing or delayed reports when interpreting geographic patterns

### 🚨 Early-Warning Signals

- Compare current case counts with agreed reference levels
- Flag unusual patterns for authorized personnel to review
- Record the reason for an alert and its review status
- Treat alerts as prompts for investigation—not as confirmation of an outbreak

### 📊 Data-Driven Insights

- Summarize suspected cases, confirmed cases, and test results
- Display trends and reporting coverage
- Support authorized aggregate reports
- Make limitations and missing data visible to users

### 🌐 Extensible Platform

- Design the system to support additional diseases and facilities
- Plan for web-based access across desktop and mobile browsers
- Allow future API integrations where approved and available
- Keep data, model, and alert-rule versions traceable

---

## 🖼️ Dashboard Reference

![](https://github.com/dr-mushtaq/Water-borne-diseases/blob/main/Images/Overview.JPG)

*User-supplied research dashboard reference. The displayed figures are reference content, not current surveillance data or results from an implemented application in this repository.*

### Proposed Dashboard Layout

| Panel | Planned Content |
| --- | --- |
| **Navigation** | Overview, Malaria, Typhoid, Hospitals & Labs, Uploads & Sync, Hotspots, Alerts, Reports |
| **Filters** | Disease, district, facility, date range, and case status |
| **Summary Cards** | Confirmed cases, suspected cases, tests performed, active alerts, reporting completeness |
| **Hotspot Map** | Geographic case distribution with reporting coverage and a separate forecast-risk layer |
| **Trend Charts** | Historical observations, future forecasts, and uncertainty intervals |
| **Hospital Reporting** | Expected submissions, latest successful sync, and validation errors |
| **Alert Management** | Trigger, severity, responsible officer, acknowledgment, and investigation status |

Filters should apply consistently across panels and exports. Missing reports must be distinguished from zero cases, and charts should have accessible table alternatives.

The patient prediction form in the reference is outside the initial operational MVP. A negative model estimate must never be displayed as proof that a patient is healthy.

---

## 🧪 Example Interaction

**Hospital Input — fictional demonstration:**

A reporting officer uploads a weekly laboratory file containing typhoid test results for patients residing in Demonstration District, Area A.

**System Processing:**

- Validate and deduplicate records.
- Summarize cases for the selected reporting period.
- Compare the aggregate with the configured surveillance threshold.
- Show reporting coverage and create an alert for officer review.

**Illustrative System Output:**

```text
Disease: Typhoid
Area: Demonstration District, Area A
Reporting Period: Most recent complete week
Reported Confirmed Cases: 24
Illustrative Reference Level: 10 cases per week
Reporting Coverage: 4 of 5 expected facilities
Alert: Configured surveillance threshold exceeded
Status: Awaiting district health officer review
Follow-up: Review data quality and investigate the increase
```

These values are fictional and do not define a validated outbreak threshold. The alert requests investigation; it does not independently confirm an outbreak.

## 🧰 Technology Stack

**Proposed design candidates — not installed dependencies or finalized technology selections.**

| Component | Candidate Tools |
| --- | --- |
| **ML and Statistical Models** | scikit-learn, XGBoost, statsmodels |
| **Data Processing** | Python, pandas, NumPy |
| **Backend** | FastAPI |
| **Frontend** | React with TypeScript; Streamlit may support an initial analytical prototype |
| **Maps and Spatial Data** | Leaflet, PostgreSQL with PostGIS |
| **Database** | PostgreSQL |
| **Background Processing** | Celery and Redis, if required by integration workloads |
| **Model and Data Versioning** | MLflow and DVC |
| **Integration** | CSV and approved APIs; HL7/FHIR adapters where supported and tested |
| **Deployment** | Docker in an approved hosted or on-premises environment |

### Candidate Models for Surveillance and Forecasting

| Approach | Input Data | Intended Use | Evaluation Considerations |
| --- | --- | --- | --- |
| **Historical or Seasonal Baseline** | Past case counts by area and reporting period | Establish a reference forecast | Required comparison for more complex models |
| **Statistical Time-Series Models** | Regularly aggregated disease counts | Estimate future case trends | Assess seasonality, reporting gaps, and forecast uncertainty |
| **Random Forest / Gradient Boosting** | Lagged counts, calendar features, and approved contextual variables | Explore nonlinear forecasting relationships | Use time-based evaluation and prevent future-data leakage |
| **Surveillance Threshold Rules** | Current observations and a defined reference level | Flag increases for investigation | Evaluate false alerts, missed events, and reporting coverage |

Medical language models are not required for the initial structured-data workflow. Extraction from free-text clinical notes may be investigated later if a defined use case, authorized data access, and a validation process justify it.

---

## 🗃️ Data Requirements

| Data Group | Example Fields | Purpose |
| --- | --- | --- |
| **Source Identity** | facility_id, source_record_id, record_updated_at | Trace records, deduplicate, and process corrections |
| **Authorized Linkage** | facility-scoped pseudonymous_patient_id, encounter_id | Link encounters and tests within the approved scope |
| **Dates** | encounter_date, specimen_date, result_date, received_at | Separate event timing from reporting delays |
| **Geography** | district_code, locality_code, facility_code | Support appropriate geographic aggregation |
| **Disease Classification** | disease_code, case_status, case_definition_version | Separate suspected and confirmed cases |
| **Laboratory Results** | test_type, result, result_status | Track test outcomes and subsequent updates |
| **Optional Demographics** | age_band, sex | Support justified aggregate subgroup analysis |
| **Provenance** | import_batch_id, source_system, schema_version | Maintain a reproducible audit trail |

Collect only data justified by the agreed surveillance purpose. Define repeat-test and disease-episode counting rules before producing totals. Facility-scoped identifiers do not establish identity across hospitals; cross-facility linkage requires a separately agreed method.

---

## 🚀 Development Plan

### Phase 1: Prototype

- Confirm pilot hospitals, districts, case definitions, and reporting workflows.
- Create a synthetic dataset and standardized CSV schema.
- Build validated uploads, disease summary cards, trend charts, and a geographic view.
- Implement configurable threshold alerts with officer acknowledgment.

### Phase 2: 🧪 Evaluation

- Validate imports, correction handling, deduplication, and aggregate totals.
- Evaluate forecasts using **MAE, RMSE, and prediction interval coverage**.
- Measure alert **precision, recall, false-alert frequency, and detection lead time** against reviewed events.
- Use held-out future periods and assess performance in withheld facilities or districts.
- Evaluate malaria and typhoid separately and compare models with seasonal baselines.
- Exclude information unavailable at prediction time and monitor reporting delays.

**No platform benchmark results are available yet.** Accuracy figures from the previous medicine recommendation project are not applicable.

### Phase 3: Enhancement

- Add historical forecasts and uncertainty displays after evaluation.
- Improve geographic analysis and reporting-completeness indicators.
- Add investigation notes, escalation, and aggregate report exports.
- Refine usability with hospital staff and district health officers.

### Phase 4: Connected Pilot and Deployment

- Integrate one approved hospital or laboratory system.
- Reconcile synchronized data with source records.
- Test notification delivery, monitoring, backups, and restoration.
- Evaluate alert usefulness and response times during a supervised pilot.
- Expand participating facilities after reviewing pilot findings.

### Phase 5: Database and Data Layer

*Begin foundational storage work during Phase 1; this phase expands and hardens it.*

- Maintain persistent storage for validated records, imports, aggregates, forecasts, and alerts.
- Implement role-based access, organization boundaries, encryption, and audit logs.
- Establish retention rules, correction workflows, and data versioning.
- Monitor missing data, schema changes, and model/data drift.
- Mark forecasts unavailable when required data are insufficient.

### Phase 6: Governance and Commercial Readiness

*Start governance planning before any live patient-data pilot.*

- Establish data-sharing authority, permitted uses, hosting arrangements, and access responsibilities.
- Review applicable local requirements with partner organizations; avoid assuming a particular regulatory classification or approval route.
- Document intended use, model limitations, evaluation results, and human review responsibilities.
- Apply aggregation and small-count suppression where needed to reduce disclosure risk.
- Define operational support, incident handling, and response ownership.
- Agree on readiness criteria before operational rollout.

This README does not certify regulatory approval or compliance with any legal framework.

## 💼 Commercial Extension

The proposed platform would serve **district health departments, hospital networks, diagnostic laboratory networks, and public health programs**.

Potential offerings include:

- Platform subscriptions for disease dashboards and alert management.
- Hospital integration, configuration, and onboarding services.
- Approved hosted or on-premises deployment options.
- Training, maintenance, and operational support.

Pricing remains to be defined with pilot partners. Early value should be measured through reporting timeliness, data quality, facility coverage, useful alerts, and time to acknowledgment and investigation. Claims about improved health outcomes require separate evaluation.

## 🔮 Future Scope

- Additional hospital and laboratory integrations.
- Additional diseases with approved case definitions and evaluation datasets.
- Weather and environmental inputs where quality and relevance are established.
- Multilingual dashboards and reporting workflows.
- Offline-assisted reporting for facilities with unreliable connectivity.
- Cross-district trend analysis and resource-planning views.
- Optional, separately validated research on patient-level risk prediction.

---

## 📚 Research Foundation

The project is inspired by [Machine learning based efficient prediction of positive cases of waterborne diseases](https://doi.org/10.1186/s12911-022-02092-1), published in *BMC Medical Informatics and Decision Making* in 2023.

The study analyzed malaria and typhoid patient records from Ayub Medical Hospital for 2017–2020 and proposed a warning/dashboard system to help health departments identify affected areas and predict positive cases.

Hospital synchronization, district forecasting, and operational alert management are proposed product extensions. The paper's patient-level classification results do not establish future outbreak forecasting performance.

📄 [Local research paper](s12911-022-02092-1.pdf)

## 📬 Contact

- **Email:** mushtaqmsit@gmail.com
- **LinkedIn:** [Mushtaq Hussain](https://www.linkedin.com/in/mushtaq-hussain-21417814/)
- **YouTube:** [Coursesteach](https://www.youtube.com/@coursesteach-mv5si)
- **Team ID:** themushtaq48

## 🤝 Contributing

Contributions in hospital integration, epidemiology, forecasting, mapping, dashboard design, and documentation are welcome. Discuss major changes before implementation, use synthetic or authorized de-identified data, and document assumptions and validation results. Keep patient records, private datasets, and credentials out of source control.

## License

The original README proposed the MIT License, but no LICENSE file is currently present. Confirm the license and add its text before distributing code. Research publications, datasets, and third-party dependencies retain their respective terms.


## 🏗️ System Architecture

### 1. Disease Surveillance and Analytics Engine

- Collect and validate disease and laboratory records from participating facilities
- Analyze suspected and confirmed cases by disease, location, and reporting period
- Compare recent case counts with historical or seasonal baselines
- Explore forecasting and hotspot-detection approaches
- Generate signals for review by authorized public health personnel

### 2. Hospital and Laboratory Reporting

- Accept standardized data through CSV uploads
- Support future integration with approved hospital and laboratory systems
- Validate required fields, dates, disease classifications, and test results
- Identify duplicate submissions and track corrections
- Report missing or delayed facility submissions

### 3. Surveillance Dashboard

- Display case summaries, trends, geographic patterns, and alerts
- Provide separate views for malaria and typhoid
- Show reporting coverage and the latest data update
- Help health teams review and investigate unusual changes

### 4. Data and Analytics Layer

- Store validated records and their source information
- Maintain aggregate summaries, model outputs, and alert history
- Support authorized reporting and reproducible evaluation
- Protect sensitive information through access controls and appropriate data handling

```mermaid
flowchart TD
    A[Hospitals and Laboratories] --> B[CSV Upload or Approved Integration]
    B --> C[Validation and Deduplication]
    C --> D[Validated Data]
    C --> E[Errors Returned for Correction]
    D --> F[Aggregation and Analysis]
    F --> G[Trend and Hotspot Monitoring]
    G --> H[Dashboard]
    G --> I[Alert for Review]
    I --> J[Authorized Public Health Team]
```

## 📌 Key Features

### 🦠 Disease Surveillance

- Monitor malaria and typhoid cases separately
- Distinguish suspected cases from confirmed cases
- Review disease trends across reporting periods and locations
- Keep observed data separate from forecasts or model estimates

### 🏥 Hospital and Laboratory Reporting

- Plan for standardized data uploads
- Validate incoming records and provide error summaries
- Track reporting completeness and data freshness
- Support future connections to approved health information systems

### 🗺️ Geographic Monitoring

- Summarize reported cases by approved district or locality boundaries
- Highlight unusual increases for further investigation
- Distinguish a patient's area of residence from the reporting facility
- Consider missing or delayed reports when interpreting geographic patterns

### 🚨 Early-Warning Signals

- Compare current case counts with agreed reference levels
- Flag unusual patterns for authorized personnel to review
- Record the reason for an alert and its review status
- Treat alerts as prompts for investigation—not as confirmation of an outbreak

### 📊 Data-Driven Insights

- Summarize suspected cases, confirmed cases, and test results
- Display trends and reporting coverage
- Support authorized aggregate reports
- Make limitations and missing data visible to users

### 🌐 Extensible Platform

- Design the system to support additional diseases and facilities
- Plan for web-based access across desktop and mobile browsers
- Allow future API integrations where approved and available
- Keep data, model, and alert-rule versions traceable

## 🧪 Example Interaction

**Illustrative example using fictional data:**

A reporting facility submits a weekly file with typhoid test results for a demonstration district.

**System processing:**

- Checks the file for required fields and invalid values
- Identifies possible duplicate records
- Summarizes reported cases for the period
- Compares the summary with an agreed surveillance reference level
- Flags an unusual increase for review

**Illustrative system output:**

```text
Disease: Typhoid
Area: Demonstration District
Reporting Period: Most recent complete week
Reported Confirmed Cases: 24
Reporting Coverage: 4 of 5 expected facilities
Signal: Configured reference level exceeded
Status: Awaiting authorized public health review
Suggested next step: Check data quality and investigate the increase
```

The example values are fictional. A signal does not independently confirm an outbreak or provide a diagnosis.

## 🧰 Technology Stack

The following are **candidate technologies for future development**, not a claim that they are already installed or used by the project.

| Component | Candidate Tools |
| --- | --- |
| **Data Analysis** | Python, pandas, NumPy |
| **Statistical Models** | statsmodels, scikit-learn |
| **Forecasting Experiments** | Seasonal baselines, time-series models, XGBoost |
| **Backend** | FastAPI or Flask |
| **Frontend / Prototype Dashboard** | Streamlit or React |
| **Database** | PostgreSQL |
| **Geographic Analysis** | Leaflet, PostGIS |
| **Data and Model Versioning** | DVC, MLflow |
| **Deployment** | Docker, subject to hosting and governance requirements |
| **Data Exchange** | CSV uploads; approved APIs where available |

### Candidate Approaches for Surveillance

| Approach | Potential Use | Evaluation Considerations |
| --- | --- | --- |
| **Historical or Seasonal Baseline** | Compare current counts with previous periods | Use as a reference before adopting more complex models |
| **Time-Series Models** | Explore future aggregate case counts | Evaluate forecast error, uncertainty, seasonality, and reporting gaps |
| **Tree-Based Models** | Explore relationships between past counts and approved contextual data | Use time-based validation and prevent data leakage |
| **Threshold-Based Signals** | Flag increases for review | Evaluate missed events, false alerts, and reporting completeness |

No model should be described as accurate or production-ready without project-specific evaluation.

## 🚀 Development Plan

### Phase 1: Prototype

- Review the available datasets, notebooks, diagrams, and project documents
- Define the disease case categories and reporting periods
- Create a documented data format; use synthetic data for early demonstrations
- Build an initial workflow for data validation and aggregate summaries
- Create a basic dashboard for trends and reporting coverage

### Phase 2: Evaluation

- Check data quality, missing values, duplicate handling, and case-counting rules
- Compare forecasting approaches with simple historical or seasonal baselines
- Use time-based test sets to evaluate forecasts on later reporting periods
- Consider MAE, RMSE, and prediction-interval coverage for forecasting
- Evaluate alert sensitivity, missed events, and false-alert frequency
- Assess malaria and typhoid separately

> Results must be reported only after evaluation on suitable project data. Results from other datasets or projects should not be presented as this project's performance.

### Phase 3: Enhancement

- Improve dashboard usability and geographic summaries
- Add reporting-completeness and data-freshness indicators
- Explore forecast visualizations with uncertainty information
- Add alert review and investigation tracking
- Collect feedback from relevant public health stakeholders

### Phase 4: Integration and Pilot

- Identify an authorized pilot partner and define permitted data use
- Test an approved hospital or laboratory data exchange
- Reconcile uploaded or synchronized records with their source
- Test monitoring, backups, access controls, and recovery procedures
- Review pilot results before considering wider deployment

### Phase 5: Data and Storage

- Define a consistent data schema and data provenance requirements
- Establish appropriate access controls, retention, and correction procedures
- Protect sensitive data and collect only what is needed for the defined purpose
- Track dataset versions and model inputs for reproducible evaluation
- Document limitations caused by missing or delayed reporting

### Phase 6: Governance and Safety

- Agree on data-sharing authority, permitted uses, and responsible personnel
- Review applicable local privacy, health-data, and regulatory requirements with qualified partners
- Document intended use, system limitations, and human review responsibilities
- Require authorized public health review before acting on surveillance signals
- Do not claim regulatory approval or legal compliance unless it has been independently established

## 🔮 Future Scope

- Integrate additional hospitals and diagnostic laboratories
- Add other diseases when suitable data and case definitions are available
- Explore environmental or weather data where its relevance and quality are established
- Add multilingual and mobile-friendly reporting workflows
- Support offline-assisted reporting for facilities with limited connectivity
- Improve district-level trend analysis and public health planning tools
- Evaluate forecasting and alerting approaches through supervised research

## 📬 Contact

For queries or collaboration:

- 📧 **Email:** mushtaqmsit@gmail.com
- 💼 **LinkedIn:** [Mushtaq Hussain](https://www.linkedin.com/in/mushtaq-hussain-21417814/)
- 🎥 **YouTube:** [Coursesteach](https://www.youtube.com/@coursesteach-mv5si)
- **Team ID:** themushtaq48

## ⭐ Support

If you find this project useful, please ⭐ star the repository and share it.

## ⚠️ Important Note

This project is intended for educational, research, and prototyping purposes.

- ❌ It does not diagnose individual patients
- ❌ It does not independently confirm an outbreak
- ❌ It should not be the sole basis for clinical or public health decisions
- ✅ Surveillance results and alerts require appropriate review by qualified personnel



# Water-borne-diseases
**Related data**
1. [Interpreting Tree-Based Model's Prediction of Individual Sample](https://coderzcolumn.com/tutorials/machine-learning/treeinterpreter-interpreting-tree-based-models-prediction-of-individual-sample?fbclid=IwAR2-zcjOO-c3XfiDoG6eufSmBaFz9mnrislreMJF6NluNUAwZZWCWtM8kYI)
2. [Malaria Detection using Deep Learning | Python Final Year IEEE Project 2020 - 2021](https://www.youtube.com/watch?v=PHK9RrYfEQ4&ab_channel=JPINFOTECHPROJECTS)
3. [Build a system to identify fake news articles!](https://medium.com/nerd-for-tech/build-a-system-to-identify-fake-news-articles-6604968043cb)
4. [END TO END Machine learning Project deployment on Flask server.](https://www.youtube.com/watch?v=PH0M8ktKCRo)
5. [Live- Implementation of End To End Kaggle Machine Learning Project With Deployment](https://www.youtube.com/watch?v=p_tpQSY1aTs&ab_channel=KrishNaik)
6. [Car-Price-Prediction](https://github.com/krishnaik06/Car-Price-Prediction/blob/master/Untitled.ipynb)
7. [venugopalkadamba Multi_Disease_Predictor](https://github.com/venugopalkadamba/Multi_Disease_Predictor)
8. [End to End Deployment of Breast Cancer Prediction Through Machine Learning using Flask](https://medium.com/analytics-vidhya/end-to-end-deployment-of-breast-cancer-prediction-through-machine-learning-using-flask-a40abbabf1fe)
9. [Build a Machine Learning web application from scratch in Python with Streamlit.](https://morioh.com/p/28f32a0d90a2?f=5c21fb01c16e2556b555ab32&fbclid=IwAR2IEef_M-c4je1UrV1XE0EX-S6NX6j1ib2b6yHAc7LPMfAxuurdzaAxxdY)
10. [ditikrushnaEnd-to-End-Diabetes-Prediction-Application-Using-Machine-Learning](https://github.com/ditikrushna/End-to-End-Diabetes-Prediction-Application-Using-Machine-Learning)
11. [Disease-Prediction-from-Symptoms](https://github.com/anujdutt9/Disease-Prediction-from-Symptoms)
