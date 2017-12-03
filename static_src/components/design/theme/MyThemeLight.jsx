import React from 'react';
import {cyan900, redA400} from 'material-ui/styles/colors';
import getMuiTheme from 'material-ui/styles/getMuiTheme';

// This replaces the textColor value on the palette
// and then update the keys for each component that depends on it.
// More on Colors: http://www.material-ui.com/#/customization/colors
export const muiTheme = getMuiTheme({
    palette: {
        primary1Color: cyan900,
        primary2Color: cyan900,
        // textColor: redA400,
    },
    appBar: {
        background: cyan900,
    },
});
