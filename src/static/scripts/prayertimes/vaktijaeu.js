  // Vaktija.eu script
  let regionNames = new Intl.DisplayNames(['en'], {type: 'region'});
  let vaktijaeu = document.currentScript.dataset.vaktijaeu.replace(/'/g, '"');
  let vaktijaeu_obj = JSON.parse(vaktijaeu);
  let countries = [];

  const contains = (array, value) => {
      for(let x = 0; x < array.length; x++) {
          if(array[x].name === value) {
              return true;
          }
      }
      return false;
  }

  const main = () =>{   
      let vaktijaeu_data = vaktijaeu_obj.data;
      // Check if data-vaktijaeu is empty
      for(let i = 0; i < vaktijaeu_data.length; i++) {
          let vaktija = vaktijaeu_data[i];
          let vaktija_slug = vaktija.slug;
          let vaktija_name = vaktija.name;
          let vaktija_country_code = vaktija.country.short_code;
          let full_country_name = regionNames.of(vaktija_country_code);
          if (contains(countries, full_country_name) != true) {
              countries.push({
                  "name": full_country_name,
                  "cities": [
                      {"name": vaktija_name, "slug": vaktija_slug}
                  ]
              });
          }
          else {
              countries.find(x => x.name == full_country_name).cities.push({"name": vaktija_name, "slug": vaktija_slug});
          }
      }
      let select = document.getElementById("vaktija_eu_country");
      countries = countries.sort((a, b) => (a.name > b.name) ? 1 : -1);
      for (let i = 0; i < countries.length; i++) {
          let option = document.createElement("option");
          option.text = countries[i].name;
          option.value = countries[i].name;
          select.appendChild(option);
          select.add(option);
      }
      select.addEventListener("change", function() {
        let cities = countries.find(x => x.name == this.value).cities;
        let select_city = document.getElementById("vaktija_eu_city");
        let vaktija_name = document.getElementById("vaktija_eu_name");
        let vaktija_button = document.querySelector("#vaktija_eu_button");
        vaktija_name.style.display = "block";
        select_city.style.display = "block";
        vaktija_button.style.display = "flex";
        select_city.innerHTML = "";


        for(let i = 0; i < cities.length; i++) {
            let option = document.createElement("option");
            option.text = cities[i].name;
            option.value = cities[i].slug;
            select_city.appendChild(option);
            select_city.add(option);
        }
      });
  }
  if(vaktijaeu_obj.data !== undefined) {
      main();
  }else {
      console.log("No data");
  }