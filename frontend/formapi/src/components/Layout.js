import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import Edit from './Edit';

// Override style 
const useStyles = makeStyles((theme) => ({
	cardMedia: {
		paddingTop: '70%', 
	},
	link: {
		margin: theme.spacing(1, 1.5),
	},
	cardHeader: {
		backgroundColor:
			theme.palette.type === 'light'
				? theme.palette.grey[200]
				: theme.palette.grey[700],
	},
	formTitle: {
		fontSize: '16px',
		textAlign: 'left',
	},
	formText: {
		display: 'flex',
		justifyContent: 'left',
		alignItems: 'baseline',
		fontSize: '12px',
		textAlign: 'left',
		marginBottom: theme.spacing(2),
	},
}));

const Layout = (props) => {
	const { layout } = props;
	const classes = useStyles();
	if (!layout || layout.length === 0) return <p>Can not find any layout, sorry</p>;
	return (
		<React.Fragment>
			<Container maxWidth="md" component="main">
				<Grid container spacing={5} alignItems="flex-end">
				{/* Reversing map elements to display the most recent image first  */}
					{layout.slice(0).reverse().map((data) => {
						return (
							<Grid item key={data.id} xs={12} md={4}>
								<Card className={classes.card}>
									<CardMedia
										className={classes.cardMedia} 
										// Checking if image url ends in either a png or jpeg format. If not then, return 404 error image
										image = {data.url}
										title="Image title"
									/>
									<CardContent className={classes.cardContent}>
										<Typography
											gutterBottom
											variant="h5"
											component="h2"
											className={classes.formTitle}
										>
										{/* Limitting the length of char input  */}
											{data.name.substr(0, 50)}
										</Typography>
										<div className={classes.formText}>
											<Typography
												component="h6"
												color="textPrimary"
											></Typography>
											<Typography variant="h6" color="textSecondary">
											{/* Limitting the length of char input  */}
												{data.caption.substr(0, 60)}
											</Typography>
										</div>
										<Edit data={data} />
									</CardContent>
								</Card>
							</Grid>
						);
					})}
				</Grid>
			</Container>
		</React.Fragment>
	);
};
export default Layout;