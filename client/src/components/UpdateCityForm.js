import {useState} from 'react'

function UpdateCityForm({updateCity, setIdToUpdate, updatePatchFormData, cities}){

    const [updateFormSubmitted, setUpdateFormSubmitted] = useState(false)

    return (
        <div className="city-form">
            <h2>Update City</h2>
            {updateFormSubmitted ? <h1>City Updated!</h1> :
            <form onSubmit={event => {
                updateCity(event)
                setUpdateFormSubmitted(updateFormSubmitted => !updateFormSubmitted)
            }}>
                <label>Choose a City: </label>
                <select onChange={(event) => {
                    setIdToUpdate(event.target.value)
                }} name="id">
                {cities.map(city => {
                    return <option key={city.id} value={city.id}>{`${city.id}: ${city.name}`}</option>
                })}
                </select>
                <input onChange={updatePatchFormData} type="text" name="name" placeholder="City name"/>
                <input onChange={updatePatchFormData} type="text" name="image" placeholder="Image URL"/>
                <input type="submit" value="Update City"/>
            </form>}
        </div>
    )
}

export default UpdateCityForm