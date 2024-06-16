console.log('attached')

function processDocument() {
    event.preventDefault();

   console.log('hello')
    var doc = document.getElementById("doc").value;
    //var doc="In a quaint village nestled in the picturesque countryside of Italy, a young boy named Leo grew up surrounded by the rich aromas and flavors of his family's bakery. For generations, the bakery had been renowned for its delectable bread and pastries, all made with love and care by Leo's family. One day, a celebrated pastry chef from a nearby city stumbled upon the bakery while exploring the village. Enchanted by the mouthwatering treats, the chef was determined to learn the secrets behind the bakery's magic. Leo's parents, though initially hesitant, eventually agreed to take the chef under their wing. Leo, fascinated by the chef's stories of the city's vibrant culinary scene, saw an opportunity to share his family's traditions with a wider audience. He convinced his parents to let him work alongside the chef, learning new techniques and recipes to elevate their bakery to new heights. As Leo honed his skills, his passion and creativity flourished. He experimented with innovative flavors and designs, infusing the bakery's classic recipes with modern twists. The chef, impressed by Leo's talent, offered him a spot in his esteemed pastry shop. Leo's family was overjoyed to see their son's dreams take flight. As Leo's creations gained popularity in the city, the village bakery became a beloved destination for foodies and locals alike. People flocked to taste Leo's signature pastries, and his family's bakery was hailed as a culinary treasure. Years passed, and Leo's bakery became a legendary institution, attracting visitors from far and wide. Leo never forgot his humble beginnings, continuing to bake with the same love and dedication that had defined his family's legacy. His story inspired a new generation of bakers, ensuring that the sweet traditions of his family's bakery would live on forever."
    console.log(doc)
    fetch('http://localhost:8080/publish_results', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        document: doc
      })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById("answer").value = data.response;
    })
    .catch(error => console.error('Error:', error));
  }