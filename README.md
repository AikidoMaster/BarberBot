
# BarberBot: A Real-Time Distributed Inquiry System for Barber Shops

## Project Overview

BarberBot Distributed is an advanced, real-time system designed to streamline customer inquiries across multiple barber shops. Leveraging distributed computing principles, this system creates an interconnected network of barber shops, enabling seamless data sharing, load balancing, and fault tolerance.

**GUI PREVIEW**

![GUI Preview](GUI.gif)

**AUTOMATED DETAILS CSV**

![AUTOMATED DETAILS CSV](CSV.png)

## Distributed Architecture

The system operates on a distributed architecture with the following components:

1. **Client Nodes**: Each barber shop functions as a client node, running a Tkinter-based GUI for inquiry submissions.

2. **Central Coordinator**: A central server manages data synchronization, load balancing, and fault tolerance across all nodes.

3. **Distributed Database**: Employs a distributed database system (e.g., Apache Cassandra) for storing and replicating inquiry data.

4. **Message Queue**: Utilizes a distributed message queue (e.g., Apache Kafka) for real-time data streaming and event-driven updates.

5. **Distributed Cache**: Uses a distributed caching system (e.g., Redis) to enhance read performance and minimize database load.

## Key Features

### 1. Real-Time Data Synchronization

Inquiry data is synchronized in real-time across all barber shops. When a customer submits an inquiry at any location, the information is instantly updated across the network.

### 2. Load Balancing

Intelligent load balancing distributes incoming inquiries evenly across all nodes, ensuring optimal resource use and preventing overload on any single node.

### 3. Fault Tolerance

Designed for fault tolerance, the system redirects traffic to other nodes if one goes offline, ensuring continuous service.

### 4. Scalability

The system easily scales to include new barber shops without disrupting existing operations, thanks to its distributed architecture.

### 5. Distributed Data Analysis

Distributed data analysis aggregates insights from all nodes, providing a comprehensive view of customer trends and preferences.

### 6. Centralized Dashboard

A real-time, centralized dashboard offers an overview of the entire network, displaying aggregated data from all barber shops.

**DASHBOARD PREVIEW**

![Dashboard Preview](dashboard.gif)

## Technical Implementation

- **Distributed Consensus**: Implements the Raft consensus algorithm to ensure consistency across nodes.
- **Peer-to-Peer Communication**: Uses gRPC for efficient peer-to-peer communication.
- **Data Partitioning**: Employs consistent hashing for efficient data distribution.
- **Distributed Transactions**: Manages distributed transactions with the two-phase commit protocol.

## Impact

BarberBot Distributed has delivered substantial benefits to barber shops:

- **Enhanced Customer Experience**: Real-time data sharing allows any barber shop to access customer history and preferences, regardless of the initial inquiry location.
- **Operational Efficiency**: Load balancing and fault tolerance optimize resource utilization and system reliability.
- **Data-Driven Insights**: Provides a comprehensive view of customer behavior across locations.
- **Scalable Growth**: Facilitates easy integration of new barber shops into the network.

## Conclusion

BarberBot Distributed marks a significant advancement in managing customer inquiries for barber shops. By applying distributed systems principles, it offers a scalable, fault-tolerant solution that improves customer experience and operational efficiency across multiple locations. Rohit Ganguly has successfully sold this solution to three local barber shops, aiding them in launching personalized ad campaigns and promotions to boost their business.
