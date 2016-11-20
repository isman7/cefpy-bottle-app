<html>
<head>
<link rel="stylesheet" href="{{host}}/static/css/bootstrap.css">
</head>
<body>
    %if name == 'World':
        <h1>Hello {{name}}!</h1>
        <p>This is a test.</p>
    %else:
        <h1>Hello {{name.title()}}!</h1>
        <p>How are you?</p>
    %end
    <br/><a href="/pid/">pid</a>
</body>
</html>