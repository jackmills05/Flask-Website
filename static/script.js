function displayLinearSearch(){
    window.location.href = "/linearsearch"
}

function showPythonLinearSearch(){
    code = document.getElementById("code")
    html = `    <code>
        def linear_search(item,items):
        for i in range(len(items)):
            if items[i] == items:
            return i 
        return False
    </code>`
    
}