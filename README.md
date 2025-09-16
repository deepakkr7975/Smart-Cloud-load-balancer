# Smart-Cloud-load-balancer


Overview
This project demonstrates a smart cloud load balancer that dynamically manages backend servers based on request load.
Load Balancer: Receives incoming requests and forwards them to backend servers using a round-robin algorithm.
Backend Servers: Simple Flask applications that respond to requests.
Dynamic Scaling: New backend servers are created when request load is high, and removed when load is low.
This setup simulates cloud auto-scaling in a practical, visual way.

Features

Round-robin load balancing

Automatic backend server scaling based on request thresholds

Manual control of servers via Docker

Future Enhancements

Streamlit dashboard for live monitoring of backend servers

Auto-scaling based on CPU/memory metrics

Deployment on cloud infrastructure for real-world demonstration

