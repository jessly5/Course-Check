<template>
  <div id="app">
	<ThePreface/>
	<div>
		
		<CourseFilter v-bind:filterSection="this.yearFilters"/>
		<CourseFilter v-bind:filterSection="this.topicFilters"/>

		<CourseCard 
			v-for="course in Object.keys(courseData).sort()"
			v-bind:key="courseData[course].courseTitleFull"
			v-bind:courseTitleFull="courseData[course].courseTitleFull"
			v-bind:courseDetails="courseData[course].courseDetails"
			v-bind:coursePrerequisites="courseData[course].coursePrerequisites"
			v-bind:tags="courseData[course].tags"
			v-bind:visible="isFilteredOut(course)"
		/>
	</div>
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
				{id: "Software", text: "Software", value: false}
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
		yearFiltersUsed: function(){
			var total = 0;
			for (var f in this.yearFilters) {
				total += this.yearFilters[f].value ? 1 : 0;
			} return total;
		},
		displayCourses: function(){
			var show = {};
			var year;
			var keys = Object.keys(courseData).sort();
			for (var k in keys){
				year = this.getYear(keys[k])-1;
				show[keys[k]] = this.yearFiltersUsed ==  0 ? true : this.yearFilters[year].value;
			}
			return show;
		}
	}
}
</script>

<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	color: #243649;
}
</style>
