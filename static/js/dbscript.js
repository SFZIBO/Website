// script.js

document.addEventListener("DOMContentLoaded", () => {
    // Toggle Sidebar
    const sidebarToggle = document.querySelector("#sidebar-toggle");
    const sidebar = document.querySelector(".sidebar");

    sidebarToggle.addEventListener("click", () => {
        sidebar.classList.toggle("collapsed");
    });

    // Render Charts
    const ctxBarChart = document.getElementById("bar-chart").getContext("2d");
    const ctxPieChart = document.getElementById("pie-chart").getContext("2d");

    // Bar Chart Configuration
    new Chart(ctxBarChart, {
        type: "bar",
        data: {
            labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            datasets: [
                {
                    label: "Profit",
                    data: [1200, 1900, 3000, 5000, 2300, 3400, 4000],
                    backgroundColor: "rgba(54, 162, 235, 0.6)",
                },
                {
                    label: "Expenses",
                    data: [1000, 1500, 2000, 3000, 1800, 2400, 3000],
                    backgroundColor: "rgba(255, 99, 132, 0.6)",
                },
            ],
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "top",
                },
            },
        },
    });

    // Pie Chart Configuration
    new Chart(ctxPieChart, {
        type: "pie",
        data: {
            labels: ["Organic", "Referral", "Direct"],
            datasets: [
                {
                    data: [55, 25, 20],
                    backgroundColor: [
                        "rgba(54, 162, 235, 0.6)",
                        "rgba(255, 205, 86, 0.6)",
                        "rgba(255, 99, 132, 0.6)",
                    ],
                },
            ],
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "top",
                },
            },
        },
    });

    // Notifications (Example Functionality)
    const notificationBell = document.querySelector("#notification-bell");
    const notifications = document.querySelector("#notifications");

    notificationBell.addEventListener("click", () => {
        notifications.classList.toggle("show");
    });

    document.addEventListener("click", (e) => {
        if (!notifications.contains(e.target) && e.target !== notificationBell) {
            notifications.classList.remove("show");
        }
    });
});
