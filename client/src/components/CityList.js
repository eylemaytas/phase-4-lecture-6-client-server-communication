import City from './City'

function CityList({cities, deleteCity, cityFocusSelector}){

    const cityComponents = cities.map((city) => {
        return <City key={city.id} city={city} deleteCity={deleteCity} cityFocusSelector = {cityFocusSelector}/>
    })

    return (
        <ul className="city-list">{cityComponents}</ul>
        )
}

export default CityList