import React from "react";

function Search({setSearchText, onlineChecker}) {



    return(
        <div className="user-input">
            <label htmlFor="search">Search Cities:</label>
            <input
                className="form"
                type="text"
                id="search"
                placeholder="Search Cities..."
                onChange={(event) => {
                    setSearchText(event.target.value)
                }}
            />
            <div>
                <select onChange={onlineChecker} name="Online">
                    <option value="all">All</option>
                    <option value={true}>Online</option>
                    <option value={false}>Offline</option>
                </select>
            </div>
        </div>
    )
}

export default Search