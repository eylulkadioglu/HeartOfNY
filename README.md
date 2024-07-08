# Heart of New York Project

This project aims to display the visitors who are standing by 'TechWorks!' building's map of New York State, the information about the historical societies in New York State . It allows people to scan the uniquely created QR codes of each county and view the historical society data of that county.

## Project Overview

This sub project of Heart of New York project also includes creation of small map of NYS with unique QR codes for each county. 

## Features

- **Interactive Map**: A small map of NYS with QR codes for each county.
- **Database Integration**: A database to store information about counties and historical societies.
- **Web-Based Application**: Seamless access to county historical information via QR code scanning.

## Installation

### Prerequisites

- Python 3.x
- PostgreSQL
- AWS Account

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/eylulkadioglu/HeartOfNY.git
    cd HeartOfNY
    ```
    
2. **Set up the database**:
    - Configure your PostgreSQL database and update the `models.py` with your database credentials.

3. **Start the server**:
    ```bash
    python app.py
    ```
    
## API

The project uses a REST API to fetch and display historical information. The API endpoints are hosted on the AWS EC2 instance.

## Technologies Used

- **Python**: For backend development.
- **PostgreSQL**: As the database system.
- **AWS EC2**: For hosting the application.
- **pgAdmin4**: For database management.
- **QR Code**: For providing interactive access to historical data.

## JavaScript Integration

In order to connect the API that is working on AWS EC2 instance, I added the following JavaScript code snippet to SquareSpace's 'Advenced' page.


```
<script>
document.addEventListener("DOMContentLoaded", function() {
    const params = new URLSearchParams(window.location.search);
    const countyId = params.get('county_id');
    if (countyId) {
        const apiUrl = `you api url`;
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const container = document.getElementById('pageWrapper');
                if (!data.societies || data.societies.length === 0) {
                    container.innerHTML = '<p style="color: red; font-size: 16px; font-weight: bold;">No societies found for this county.</p>';
                    return;
                }
                const countyName = data.county_name || 'Unknown County'; 
                const header = `<h1 style="font-size: 24px; font-weight: bold; margin-bottom: 20px;">${countyName}, NY</h1>`;
                const societies = data.societies.map(s => {
                    const website = s.website ? `<a href='${s.website}' style="color: blue; text-decoration: none;">Click</a>` : 'Not available';
                    return `
                        <li style="margin-bottom: 10px; list-style-type: none; padding: 5px; border-bottom: 1px solid #ccc;">
                            <strong>Name:</strong> ${s.name} <br>
                            <strong>Website:</strong> ${website}<br>
                            <strong>Address:</strong> ${s.location} 
                        </li>
                    `;
                }).join('');
                container.innerHTML = `${header}<ul style="padding: 0; margin: 20px 0;">${societies}</ul>`;
            })
            .catch(error => {
                console.error('Failed to fetch societies:', error);
                document.getElementById('pageWrapper').innerHTML = '<p style="color: red; font-size: 16px; font-weight: bold;">Error loading societies.</p>';
            });
    }
});
</script>
```

This code fetches data from the API hosted on the EC2 instance and displays it on the Squarespace page. Make sure to replace 'your api url' with the actual endpoint you are using.

