import {
    EDIT_BUTTON_PREFIX,
    addItemToPage,
    clearInputs,
    renderItemsList,
    getInputValues,
} from "./dom_util.js";
import {getAllSportBuilds, createSportBuild, updateSportBuild, deleteSportBuild} from "./api.js";

const submitButton = document.getElementById("submit_button");

let sportBuilds = [];

const onEditItem = async (e) => {
    const itemId = e.target.id.replace(EDIT_BUTTON_PREFIX, "");

    await updateSportBuild(itemId, getInputValues())

    clearInputs();

    refetchAllSportBuilds();
};

const onRemoveItem = (id) => deleteSportBuild(id).then(refetchAllSportBuilds);

export const refetchAllSportBuilds = async () => {
    const allSportBuilds = await getAllSportBuild();

    sportBuilds = allSportBuilds;

    renderItemsList(sportBuilds, onEditItem, onRemoveItem);
};

submitButton.addEventListener("click", (event) => {
    event.preventDefault();

    const {title, description} = getInputValues();

    clearInputs();

    createSportBuild({
        title,
        description,
    }).then(refetchAllSportBuilds);
});

refetchAllSportBuilds();
