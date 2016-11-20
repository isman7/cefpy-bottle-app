<html>
<head>
    <link rel="stylesheet" href="{{host}}/static/css/bootstrap.min.css">
    <link rel="stylesheet" href="{{host}}/static/css/font-awesome.min.css">
</head>
<body>
    %if name == 'World':
        <h1>Hello {{name}}!</h1>
        <p>This is a test. Font Awesome also: <i class="fa fa-address-card" aria-hidden="true"></i></p>
    %else:
        <h1>Hello {{name.title()}}!</h1>
        <p>How are you?</p>
    %end
    <br/><a href="/pid/">pid</a>
</body>
</html>