console.log('If you like to contribute to this project check out the repo')

const populateSearch = data =>{
    let ul = document.getElementById('searchList')
    data.forEach((element, i) => {
        let li = document.createElement('li')

        let a = document.createElement('a')
        a.href = '#'+ i + '_details'

        let type = document.createElement('span')
        let searchText = document.createElement('span')


        ul.appendChild(li)
        li.appendChild(a)

        type.innerText = element.type
        type.className = 'tag'

        searchText.className = 'searchText'
        searchText.innerText = element.name

        a.appendChild(searchText)
        a.appendChild(type)
        
    });
}

const populateDetails = data =>{
 let details = document.getElementById('details');
 data.forEach((elem, i)=>{

     let contentDiv = document.createElement('div');
     contentDiv.className = 'contentDiv'

     let heading = document.createElement('h3')
     heading.innerText = '## '+ elem.name
     heading.id = i + '_details';

     let description = document.createElement('p')
     description.innerHTML = elem.description

     details.appendChild(contentDiv)
     contentDiv.appendChild(heading)
     contentDiv.appendChild(description)

     
     if(elem.usage !== undefined){
        let usage = document.createElement('code')
        usage.className = 'usage'
        usage.innerHTML = elem.usage
        contentDiv.appendChild(usage)
    }
 })

}

document.onreadystatechange = () => {
    // document ready
    if (document.readyState === 'complete') {
    
        fetch('data.json')
        .then(response => response.json())
        .then(data=>{
            window.data = data;
            populateSearch(data)
            populateDetails(data)
        })

    // Filter li as user types in search box
        let e = document.getElementById('search');
        e.oninput = e=>{
            let ul = document.getElementById('searchList')
            let li = ul.getElementsByTagName("li");
            let filter = document.getElementById('search').value.toLowerCase();
            // Hide elements that does not match search term
            Array.from(li).forEach(elem=>{
                const text = elem.getElementsByClassName("searchText")[0].innerHTML.toLowerCase();
                const tag = elem.getElementsByClassName("tag")[0].innerHTML.toLowerCase();
                
                if (text.indexOf(filter) > -1 ||
                    tag.indexOf(filter) > -1) {
                    elem.style.display = "";
                } else {
                    elem.style.display = "none";
                }

            })

        }
        
    }
  };