# IoT Data Processing Platform

## 1. Project Overview
The IoT Data Processing Platform simulates storing, analyzing, and visualizing data collected by IoT devices. The project focuses on key aspects of software development:

- **Data Generation**
- **Database Management**
- **Data Analysis with an ML Model**
- **Visualization**
- **Testing** (unit and end-to-end testing)

---

## 2. Testing and Problem Solving
Testing started with unit tests and expanded to end-to-end tests, covering the entire system functionality. This transition required:

- **Refactoring code** to ensure seamless integration of components.
- **Expanding test coverage** to include critical functionality.
- **Problem-solving sessions** to address compatibility issues between the database and visualization functions.

---

## 3. Project Components

### Data Generation
- Implemented `generate_sensor_data()` to simulate random IoT data.
- Standardized the data structure to meet database requirements.

### Database Management
- Developed `save_sensor_data()`, `fetch_all_data()`, and `clear_database()` for data management.
- Fixed duplicate data issues and ensured database clearing in tests.

### Data Analysis
- Created `analyze_data()` to calculate averages for data analysis.
- Adjusted data formats to ensure compatibility with the analysis function.

### Visualization
- Implemented `visualize_data()` to plot graphs for temperature, humidity, and pressure.
- Modified the function to save visualizations to files (`plt.savefig()`) instead of opening a GUI window, enabling automated testing.

### End-to-End Testing
- Tested the entire workflow from data generation to visualization:
  - **Data Generation:** Verified the creation of 10 data points.
  - **Database Storage:** Ensured all data was saved to the database.
  - **Analysis:** Confirmed the analysis function returned valid results.
  - **Visualization:** Verified that graphs were saved to files.

---

## 4. CI/CD Pipeline
**Why:** To automate testing and development processes.  
**How:**
- Created a GitHub Actions-based CI/CD pipeline that:
  - Installs dependencies.
  - Runs automated tests.
- Resolved initial issues, such as missing files and dependencies.

---

## 5. How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shambbaz/IoT-Data-Processing.git
   cd IoT-Data-Processing
2. Create and activate a virtual environment:
 ```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


3. Install depencies pip install -r requirements.txt

4. Run tests:
```bash
pytest tests/


5. Run the application: Execute each script as needed
```bash
python data_generator.py
python data_storage.py
python ml_model.py
python data_visualizer.py
