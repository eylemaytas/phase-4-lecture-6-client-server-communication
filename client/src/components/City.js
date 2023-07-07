function City({city, deleteCity}){
    return (
        <li className="city">
            <h1>City # {city.id}: {city.name}</h1>
            <img src={city.image} alt={city.name} />
            <button onClick={() => deleteCity(city.id)}>Delete City # {city.id}</button>
        </li>
    )
}

export default City