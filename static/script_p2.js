function fetchCompletedOrders() {
    $.getJSON('/get_completed_orders', function(data) {
        // Update Processed Count
        $('#processed').text(data.completed_orders.length);

        // Update Completed Orders Table
        let completedOrdersHTML = "";
        data.completed_orders.forEach(order => {
            completedOrdersHTML += `
                <tr>
                    <td>${order.id.slice(24)}</td>
                    <td>${order.productionStartTime}</td>
                    <td>${order.productionEndTime}</td>
                    <td>${order.productionLocation}</td>
                    <td>${order.orderQuantity}</td>
                </tr>
            `;
        });
        $('#current-batch').html(completedOrdersHTML);
    });
}

$(document).ready(function() {
    setInterval(fetchCompletedOrders, 10000); // Fetch completed orders every second
});