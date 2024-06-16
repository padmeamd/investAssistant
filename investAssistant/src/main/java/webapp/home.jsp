<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="form" %>
<%@ taglib uri="http://www.springframework.org/tags" prefix="spring" %>
<%@ taglib uri="http://www.thymeleaf.org" prefix="th" %>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Investment Assistant</title>
    <link rel="stylesheet" href="<c:url value='/resources/css/style.css'/>">
</head>
<body>
<div>
    <h1>Welcome to Investment Assistant</h1>
    <p>This is the home page of the Investment Assistant application.</p>

    <h2>Get Recommendations</h2>
    <form id="criteriaForm" action="${pageContext.request.contextPath}/api/recommend" method="post">
        <label for="criteria">Enter Criteria:</label>
        <input type="text" id="criteria" name="criteria" required>
        <button type="submit">Get Recommendations</button>
    </form>

    <div id="recommendations">
        <!-- Recommendations will be displayed here -->
    </div>
</div>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
    $(document).ready(function() {
        $('#criteriaForm').on('submit', function(e) {
            e.preventDefault();
            $.ajax({
                url: '${pageContext.request.contextPath}/api/recommend',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({
                    criteria: $('#criteria').val()
                }),
                success: function(response) {
                    $('#recommendations').html(response);
                }
            });
        });
    });
</script>
</body>
</html>
