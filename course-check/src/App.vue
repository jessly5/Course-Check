<template>
	<div id="app">
		<ThePreface/>
		
		<div class="container">
			<div id="filters">
				<h2 class="filterLabel">I'm looking for:</h2>
				
				<CourseFilter 
					v-bind:filterGroupName="'year'"
					v-bind:filterTitle="'Filter by year:'"
					v-bind:filterOptions="this.yearFilters"
				/>
				<CourseFilter 
					v-bind:filterGroupName="'topic'"
					v-bind:filterTitle="'Filter by topic:'"
					v-bind:filterOptions="this.topicFilters" 
				/>
				
				<span><a href="#filters"><button id="stickyTop">Back to Top</button></a></span>
			</div>
			
			<div>
				<h2 class="searchLabel">Search Results</h2>
				
				<CourseCard 
					v-for="course in courseKeys"
					v-bind:key="courseData[course].courseTitleFull"
					v-bind:courseTitleFull="courseData[course].courseTitleFull"
					v-bind:courseDetails="courseData[course].courseDetails"
					v-bind:coursePrerequisites="courseData[course].coursePrerequisites"
					v-bind:tags="courseData[course].tags"
					v-bind:visible="isFilteredOut(course)"
				/>
			</div>
		</div>
		
		<footer><a href="https://github.com/jessly5/Course-Check"><img src="./assets/GitHub_Logo.png" alt="GitHub Logo" height="30px"></a></footer>
	</div>
</template>

<script>
import ThePreface from './components/ThePreface.vue'
import CourseCard from './components/CourseCard.vue'
import CourseFilter from './components/CourseFilter.vue'
import courseData from './json/course-data.json'

export default {
	name: 'App',
	data(){
		return {
			courseData: courseData,
			yearFilters: [
				{id: "firstYearFilter", text: "1st year", value: false},
				{id: "secondYearFilter", text: "2nd year", value: false},
				{id: "thirdYearFilter", text: "3rd year", value: false},
				{id: "fourthYearFilter", text: "4th year", value: false}
			],
			topicFilters: [
				{id: "Advertising", text: "Advertising", value: false},
				{id: "Design", text: "Design", value: false},
				{id: "Experiential", text: "Experiential", value: false},
				{id: "Game", text: "Game", value: false},
				{id: "Human", text: "Human", value: false},
				{id: "Internship", text: "Internship", value: false},
				{id: "Management", text: "Management", value: false},
				{id: "Marketing", text: "Marketing", value: false},
				{id: "Media", text: "Media", value: false},
				{id: "Politics", text: "Politics", value: false},
				{id: "Programming", text: "Programming", value: false},
				{id: "Research", text: "Research", value: false},
				{id: "Software", text: "Software", value: false},
				{id: "None", text: "No Tags", value: false}
			]
		}
	},
	components: {
		ThePreface,
		CourseCard,
		CourseFilter
	},
	methods: {
		isFilteredOut: function(course){
			return (this.displayCourses[course]);
		},
		getYear: function(course){
			return parseInt(course.slice(3, 4));
		}
	},
	computed: {
		courseKeys: function(){
			return Object.keys(courseData).sort();
		},
		totalYearFiltersUsed: function(){
			var total = 0;
			for (var f in this.yearFilters) {
				total += this.yearFilters[f].value ? 1 : 0;
			} return total;
		},
		applyYearFilters: function(){
			var list = {};
			var year;
			for (var k in this.courseKeys){
				year = this.getYear(this.courseKeys[k])-1;
				list[this.courseKeys[k]] = this.totalYearFiltersUsed ==  0 ? true : this.yearFilters[year].value;
			}
			return list;
		},
		totalTopicFiltersUsed: function(){
			var total = 0;
			for (var f in this.topicFilters) {
				total += this.topicFilters[f].value ? 1 : 0;
			} return total;
		},
		applyTopicsFilter: function(){
			var list = {};
			var topic, courseTags;
			for (var k in this.courseKeys){
				for (var t in this.topicFilters){
					topic = this.topicFilters[t].id;
					courseTags = this.courseData[this.courseKeys[k]].tags;
					
					if (courseTags.includes(topic) && this.topicFilters[t].value){
						list[this.courseKeys[k]] = true;
					} else{
						list[this.courseKeys[k]] = list[this.courseKeys[k]] ? list[this.courseKeys[k]] : false;
					}
				}
			} return list;
		},
		displayCourses: function(){
			if ((this.totalYearFiltersUsed + this.totalTopicFiltersUsed == 0) || (this.totalTopicFiltersUsed == 0)) {
				return this.applyYearFilters;
			} if (this.totalYearFiltersUsed == 0){
				return this.applyTopicsFilter;
			}
			
			var list = {}
			for (var k in this.courseKeys){
				list[this.courseKeys[k]] = this.applyYearFilters[this.courseKeys[k]] && this.applyTopicsFilter[this.courseKeys[k]];
			} return list;
		}
	}
}
</script>

<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	color: #243649;
}
footer {
	text-align: center;
	clear: both;
}
#filters {
	margin-right: 1em;
	width: 200px;
}
.filterLabel {
}
.searchLabel {
	text-align: right;
}
#stickyTop {
	text-align: center;
	position: sticky;
	position: -webkit-sticky;
	top: 1em;
	background: #243649;
	border: none;
	border-radius: 1em;
	color: #F7F9F9;
	padding: 0.7em;
	font-size: 1em;
	float: left;
	margin: 1em 1em 0 0;
}
#stickyTop:hover {
	background: #0DBDB4;
}
.container {
	display: grid;
	grid-template-columns: auto auto;
}
@media only screen and (max-width: 640px) {
	#filters {
		width: 100%;
	}
	.searchLabel {
		float: none;
		text-align: left;
	}
	.container {
		display: static;
		grid-template-columns: auto;
	}
}
</style>
