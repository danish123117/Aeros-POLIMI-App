document.addEventListener('DOMContentLoaded', function () {
    const startBtn = document.getElementById('start-batch');
    const endBtn = document.getElementById('complete-batch');
    startBtn.addEventListener('click', function () {
        const mode = document.getElementById('mode').value;  // Get selected mode from dropdown
        fetch('/start_production', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ mode: mode })  // Send mode in the request body
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                startBtn.disabled = true;
                fetchOrders();
            } else {
                alert('Failed to start production:No orders available');
            }
        });
    });

    endBtn.addEventListener('click', function () {
        fetch('/complete_production', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                endBtn.disabled = true;
                fetchOrders();
            } else {
                alert('Failed to complete production:No orders available');
            }
        });
    });
    
    function fetchOrders() {
        fetch('/get_orders')
        .then(response => response.json())
        .then(data => {
            // Update counts
            document.getElementById('waiting').textContent = data.incomplete_orders.length;
            document.getElementById('inprocess').textContent = data.processing_orders.length;
            document.getElementById('processed').textContent = data.completed_orders.length;
    
            // Update Current Batch Table
            const currentBatchBody = document.getElementById('current-batch');
            currentBatchBody.innerHTML = '';
            data.processing_orders.forEach(order => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${order.id.slice(24)}</td>
                    <td>${order.productionStartTime}</td>
                    <td>${order.orderQuantity}</td>
                `;
                currentBatchBody.appendChild(row);
            });
    
            // Update Waiting List Table
            const waitingListBody = document.getElementById('waiting-list');
            waitingListBody.innerHTML = '';
            data.incomplete_orders.forEach(order => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${order.id.slice(24)}</td>
                    <td>${order.creationTime}</td>
                    <td>${order.orderQuantity}</td>
                `;
                waitingListBody.appendChild(row);
            });
    
            // Enable/Disable buttons based on order state
            if (data.processing_orders.length > 0) {
                startBtn.disabled = true;   
                                    
            } else {
                startBtn.disabled = false;
            }
        });
    }
    

    // Initial fetch and auto-update every 3 seconds
    fetchOrders();
    setInterval(fetchOrders, 5000);
});
