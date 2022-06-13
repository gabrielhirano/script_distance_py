var inputValor = document.getElementById('valor');
lati = -19.963404, long = -44.20023; // Coordenadas iniciais do mapa
zoom = 13; // zoom inicial
position = { lat: lati, lng: long};
marcador = false; // para verificar se o marcador ja existe
var enderecoTratado;
var houseNumber;
var street;
var typeLogradouro = "";



ler.readAsText("dados.csv")

function searchStreet(str){ // Função para identificar o logradouro
  layers = ["rua", "estrada", "via", "avenida", "rodovia", "alameda", "acesso", "beco", "praca", "viaduto", "travessa", "trevo"];
  for(let i = 0; i < layers.length; i++){
    if(str.replace(layers[i],'')){
      typeLogradouro = layers[i];
      str = str.replace(/\d+/g, '').slice(0,-1);
      return str.replace(layers[i],'').slice(1);
    }
  }
  return null;
}

function levDist(str1, str2){ // retorna a quantidade de operações necessarias para as duas strings serem iguais 
  const grid = [];
  for(let i = 0; i < str1.length + 1; i++){
    const row = [];
    for(let j = 0; j < str2.length + 1; j++){
      row.push(j);
    }
    row[0] = i;
    grid.push(row);
  }
  for(let i = 1; i < str1.length + 1; i++){
    for(let j = 1; j < str2.length + 1; j++){
      if(str1[i - 1] === str2[j - 1]){
        grid[i][j] = grid[i - 1][j-1];
      } else {
        grid[i][j] = 1 + Math.min(grid[i-1][j-1], grid [i-1][j], grid[i][j-1]);
      }
    }
  }
  return grid[str1.length][str2.length];
}

function searchCoord(obj){
  
  if(houseNumber != null){
    if(obj.features[0].properties.housenumber == houseNumber){
      return { lng: obj.features[0].geometry.coordinates[0], lat: obj.features[0].geometry.coordinates[1]};
    }
  } else {
    let label = obj.features[0].properties.label.slice(0,obj.features[0].properties.label.indexOf(',')).toLowerCase();

    if(levDist(label,enderecoTratado) <= 2 || label.includes(enderecoTratado)){
      houseNumber = obj.features[0].properties.housenumber;
      street = obj.features[0].properties.street;
      return { lng: obj.features[0].geometry.coordinates[0], lat: obj.features[0].geometry.coordinates[1]};
    }
  }
  alert('Numero não encontrado');
  return null;
}

function trataInput(input){
  // Tratando endereço para pesquisa
  enderecoTratado = input.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  enderecoTratado = input.toLowerCase();
  enderecoTratado = enderecoTratado.replace('z','s');
  enderecoTratado = enderecoTratado.replace('ss','s');
  enderecoTratado = enderecoTratado.replace('  ',' ');
  enderecoTratado = enderecoTratado.replace('ç','c');

  street = searchStreet(enderecoTratado)
  houseNumber = input.match(/(\d+)/);

  // Uma das maneiras para descobrir se é um local ou endereço.
  if(houseNumber != null){
    houseNumber = houseNumber[0];
    let addres = `http://geoteste:4000/v1/search?text=${enderecoTratado}&size=1&focus.point.lat=-19.94150&focus.point.lon=-44.19809&boundary.circle.lat=-19.94150&boundary.circle.lon=-44.198091&boundary.circle.radius=15&layers=${typeLogradouro}`;
    return addres;

  }else{
    let place = `http://geoteste:4000/v1/autocomplete?text=${enderecoTratado},betim&size=1&focus.point.lat=-19.94150&focus.point.lon=-44.19809&boundary.circle.lat=-19.94150&boundary.circle.lon=-44.198091&boundary.circle.radius=15`;
    return place;

  }
}

function salvaNome(evt){
  if(window.event.key == 'Enter'){
    fetch(trataInput(inputValor.value))
    .then(function (resp) {
      return resp.json();
    })
    .then(function(data){
      obj = data;
      console.log(data)
      if(obj.features.length != 0){
        position = searchCoord(obj);
        if(marcador == false){
          long = data.features[0].geometry.coordinates[0];
          lati = data.features[0].geometry.coordinates[1];
          zoom = 19;
          marcador = true;
          
          // position = { lat: -19.950937080224293, lng: -44.18835958735184};
          
          initMap()  
        }
      } else {
        alert('Endereço não encontrado');
        console.log("endereço não encontrado");
      }
    });
  }
}

// key = AIzaSyCpaiuSarCTq4h0utLsJR1w28iZ9vARXhQ

// Initialize and add the map
function initMap() {
    // The location of Uluru

    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: zoom,
      center: position,
    });
    // The marker, positioned at Uluru
    if(marcador == true){
      const marker = new google.maps.Marker({
        position: position,
        map: map,
      });
      
      marcador = false;  
    }
  }