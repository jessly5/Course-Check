<template>
	<div>
		<div v-for="filter in filterSection" v-bind:key="filter.id">
			<input v-model="filter.value" type="checkbox" id="filter.id" value="filter.id" name="filter.id">
			<label for="filter.id">{{ filter.text }}</label>
		</div>
	</div>
</template>

<script>
export default {
	name: 'CourseFilter',
	props: {
		filterSection: Array
	}
}
</script>

<style scoped>
</style>
