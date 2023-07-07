import {useState} from 'react'

function NewCityForm({addCities, updatePostFormData}){

    const [formSubmitted, setFormSubmitted] = useState(false)

    return (
        <div className="city-form">
            <h2>Add New City</h2>
            {formSubmitted ? <h1>Thanks for adding a new city!</h1> :
            <form onSubmit={event => {
                addCities(event)
                setFormSubmitted(formSubmitted => !formSubmitted)
            }}>
                <input onChange={updatePostFormData} type="text" name="name" placeholder="City name" required/>
                <input onChange={updatePostFormData} type="text" name="image" placeholder="Image URL" required/>
                <input type="submit" value="Add City"/>
            </form>}
        </div>
    )
}

export default NewCityForm