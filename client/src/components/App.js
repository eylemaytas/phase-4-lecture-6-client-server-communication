import '../App.css';
import {useState, useEffect} from 'react'
import { Route, Switch } from "react-router-dom"

import NavBar from './NavBar'
import Header from './Header'
import CityList from './CityList'
import NewCityForm from './NewCityForm'
import UpdateCityForm from './UpdateCityForm'

function App() {

  const [cities, setCities] = useState([])
  const [postFormData, setPostFormData] = useState({})
  const [idToUpdate, setIdToUpdate] = useState(0)
  const [patchFormData, setPatchFormData] = useState({})

  useEffect(() => {
    fetch('/cities')
    .then(response => response.json())
    .then(citiesData => setCities(citiesData))
  }, [])

  useEffect(() => {
    if(cities.length > 0 && cities[0].id){
      setIdToUpdate(cities[0].id)
    }
  }, [cities])

  function addCities(event){
    event.preventDefault()

    fetch('/cities', {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(postFormData)
    })
    .then(response => response.json())
    .then(newCity => setCities(cities => [...cities, newCity]))
  }

  function updateCity(event){
    event.preventDefault()
    fetch(`/cities/${idToUpdate}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(patchFormData)
    })
    .then(response => response.json())
    .then(updatedCity => {
      setCities(cities => {
        return cities.map(city => {
          if(city.id === updatedCity.id){
            return updatedCity
          }
          else{
            return city
          }
        })
      })
    })
  }

  function deleteCity(id){
    fetch(`/cities/${id}`, {
      method: "DELETE"
    })
    .then(() => setCities(cities => {
      return cities.filter(city => {
        return city.id !== id
      })
    }))
  }

  function updatePostFormData(event){
    setPostFormData({...postFormData, [event.target.name]: event.target.value})
  }

  function updatePatchFormData(event){
    setPatchFormData({...patchFormData, [event.target.name]: event.target.value})
  }


  // return (
  //   <div className="app">
  //     <div className='header'>
  //       <Header logoClick={logoClick} />
  //       <Nav />
  //     </div>
  //     <Switch>
  //       <Route exact path="/">
  //         <Login />
  //       </Route>
  //       <Route exact path="/home">
  //         <Homepage manufacturerFocusSelector={manufacturerFocusSelector}/>
  //       </Route>
  //       <Route exact path="/cities">
  //         <CityList cityFocusSelector={cityFocusSelector} cities={cities}/>
  //         <Search setSearchText={setSearchText} onlineChecker={onlineChecker} />
  //       </Route>
  //       <Route exact path="/foods">
  //         <FoodList foods={filteredFoods} foodFocusSelector={foodFocusSelector} />
  //       </Route>
  //       <Route exact path="/continents">
  //         <ContinentList continents={continents} continentFocusSelector={continentFocusSelector} />
  //       </Route>
  //       <Route exact path="/devicefocus">
  //         <DeviceFocus focusDevice={focusDevice} />
  //       </Route>
  //       <Route exact path="/developerfocus">
  //         <DeveloperFocus focusDeveloper={focusDeveloper} />
  //       </Route>
  //       <Route exact path="/gamefocus">
  //         <GameFocus focusGame={focusGame}/>
  //       </Route>
  //       <Route exact path='/manufacturerfocus'>
  //         <ManufacturerFocus deviceFocusSelector={deviceFocusSelector} focusManufacturer={focusManufacturer} />
  //       </Route>
  //       <Route exact path='/relationships'>
  //         <RelationshipManager relationshipButton={relationshipButton} />
  //       </Route>
  //       <Route exact path='/relationships/new_relationship'>
  //         <NewRelationship addRelationship={addRelationship} updateNewRelationship={updateNewRelationship}/>
  //       </Route>
  //       <Route exact path="/games/new_game">
  //         <NewGameForm  updateFormData={updateFormData} addGame={addGame}/>
  //       </Route>
  //     </Switch>
  //     <Footer />
  //   </div>
  // );

  return (
    <div className="app">
      <NavBar/>
      <Header />
      <Switch>
        <Route exact path="/continents">
          <h1>Continents:</h1>
        </Route>
        <Route path="/cities">
          <CityList cities={cities} deleteCity={deleteCity} addCities = {addCities} updatePostFormData={updatePostFormData}/>
          <NewCityForm addCity={addCities} updatePostFormData={updatePostFormData}/>
          <UpdateCityForm updateCity={updateCity} setIdToUpdate={setIdToUpdate} updatePatchFormData={updatePatchFormData} cities={cities}/>
        </Route>
        <Route path="/foods">
        </Route>

        <Route path="/blogs">
        </Route>
      </Switch>
    </div>
  );
}

export default App;
