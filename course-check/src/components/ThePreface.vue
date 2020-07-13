<template>
	<div class="preface">
		<h1>Course Checker</h1>
		
		<button type="button" id="about" v-on:click="filterCollapse">About</button>
		
		<div id="text" v-if="about">
			<h3>What is this?</h3>
			<p>This tool displays and filters data scraped from the UTM timetable for the 2020-2021 fall/winter session (with the exception of a hard coded course that is only offered in the summer). It currently focuses on courses for the CCIT major, which excludes any course not beginning with CCT and any course that has a restriction to exclude CCIT majors.</p>		
				
			<h3>Why did you build this?</h3>
			<p>Currently the official UTM timetable displays CCIT, DEM, and PWC program courses under on subject area due to them being offered by the same department. However, I am only interested in courses that a CCIT major can take. Having to scroll through courses I am restricted from taking or simply not for my program is annoying. For example, most course codes starting with MGD or include DEM in the title will not allow CCIT majors to enroll.</p>
		</div>
	</div>
</template>

<script>
export default {
	name: 'ThePreface',
	data(){
		return {
			about: false
		}
	}, 
	methods: {
		filterCollapse: function(){
			this.about = this.about ? false : true;
		}
	}
}
</script>

<style scoped>
.preface {
	margin: 1.5em;
}
#about {
	color: #F7F9F9;
	background: #243649;
	text-align: center;
	border: none;
	border-radius: 1em;
	padding: 0.7em;
	font-size: 1em;
}
#about:hover {
	background: #0DBDB4;
}
@media only screen and (max-width: 500px) {
	#about {
		width: 100%;
	}
}
</style>
