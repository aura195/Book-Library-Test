<!-- src/pages/AdminBookLoan.vue -->

<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <header class="bg-white shadow-sm border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center py-6">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <h1 class="text-2xl font-bold text-gray-900 flex items-center">
                <span class="text-primary-600 mr-2">📚</span>
                Library Management
              </h1>
            </div>
          </div>
          <div class="flex items-center space-x-4">
            <button 
              @click="loadBookLoans" 
              class="btn btn-secondary flex items-center"
            >
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
              </svg>
              Refresh
            </button>
            <button 
              @click="showCreateDialog = true" 
              class="btn btn-primary flex items-center"
            >
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
              </svg>
              New Loan
            </button>
          </div>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Statistics Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div class="card p-6">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <div class="w-8 h-8 bg-primary-100 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
                </svg>
              </div>
            </div>
            <div class="ml-4">
              <p class="text-sm font-medium text-gray-500">Total Loans</p>
              <p class="text-2xl font-bold text-gray-900">{{ statistics.total_loans }}</p>
            </div>
          </div>
        </div>

        <div class="card p-6">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <div class="w-8 h-8 bg-warning-100 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-warning-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
            </div>
            <div class="ml-4">
              <p class="text-sm font-medium text-gray-500">Active Loans</p>
              <p class="text-2xl font-bold text-gray-900">{{ statistics.active_loans }}</p>
            </div>
          </div>
        </div>

        <div class="card p-6">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <div class="w-8 h-8 bg-danger-100 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-danger-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z"></path>
                </svg>
              </div>
            </div>
            <div class="ml-4">
              <p class="text-sm font-medium text-gray-500">Overdue</p>
              <p class="text-2xl font-bold text-gray-900">{{ statistics.overdue_loans }}</p>
            </div>
          </div>
        </div>

        <div class="card p-6">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <div class="w-8 h-8 bg-success-100 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-success-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
            </div>
            <div class="ml-4">
              <p class="text-sm font-medium text-gray-500">Returned</p>
              <p class="text-2xl font-bold text-gray-900">{{ statistics.returned_loans }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Filters and Search -->
      <div class="card p-6 mb-8">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Student Name</label>
            <input 
              v-model="filters.student_name" 
              type="text"
              placeholder="Filter by student name..."
              class="input"
              @input="loadBookLoans"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Book Title</label>
            <input 
              v-model="filters.book_title" 
              type="text"
              placeholder="Filter by book title..."
              class="input"
              @input="loadBookLoans"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Status</label>
            <select v-model="filters.is_returned" @change="loadBookLoans" class="select">
              <option value="">All Status</option>
              <option value="false">Active</option>
              <option value="true">Returned</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="flex justify-center items-center py-12">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>

      <!-- Error State -->
      <div v-if="error" class="bg-danger-50 border border-danger-200 rounded-lg p-4 mb-6">
        <div class="flex">
          <div class="flex-shrink-0">
            <svg class="h-5 w-5 text-danger-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z"></path>
            </svg>
          </div>
          <div class="ml-3">
            <p class="text-sm text-danger-800">{{ error }}</p>
          </div>
        </div>
      </div>

      <!-- Book Loans Table -->
      <div v-if="!loading" class="card overflow-hidden">
        <div class="px-6 py-4 border-b border-gray-200">
          <h3 class="text-lg font-medium text-gray-900">Book Loans</h3>
        </div>
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Student</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Book</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Loan Date</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Due Date</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Return Date</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr 
                v-for="loan in bookLoans" 
                :key="loan.id" 
                :class="{ 'bg-warning-50': isOverdue(loan) }"
                class="hover:bg-gray-50 transition-colors duration-150"
              >
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 h-10 w-10">
                      <div class="h-10 w-10 rounded-full bg-primary-100 flex items-center justify-center">
                        <span class="text-sm font-medium text-primary-600">{{ loan.student.name.charAt(0) }}</span>
                      </div>
                    </div>
                    <div class="ml-4">
                      <div class="text-sm font-medium text-gray-900">{{ loan.student.name }}</div>
                      <div class="text-sm text-gray-500">{{ loan.student.student_id }}</div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm font-medium text-gray-900">{{ loan.book.title }}</div>
                  <div class="text-sm text-gray-500">by {{ loan.book.author }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {{ formatDate(loan.loan_date) }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {{ formatDate(loan.due_date) }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {{ loan.return_date ? formatDate(loan.return_date) : '-' }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span :class="getStatusClasses(loan)" class="inline-flex px-2 py-1 text-xs font-semibold rounded-full">
                    {{ getStatusText(loan) }}
                  </span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex space-x-2">
                    <button 
                      v-if="!loan.is_returned" 
                      @click="markAsReturned(loan.id)"
                      class="btn btn-success btn-sm flex items-center"
                      title="Mark as returned"
                    >
                      <svg class="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                      </svg>
                      Return
                    </button>
                    <button 
                      @click="editLoan(loan)" 
                      class="btn btn-warning btn-sm flex items-center"
                      title="Edit loan"
                    >
                      <svg class="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path>
                      </svg>
                      Edit
                    </button>
                    <button 
                      @click="deleteLoan(loan.id)" 
                      class="btn btn-danger btn-sm flex items-center"
                      title="Delete loan"
                    >
                      <svg class="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                      </svg>
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </main>

    <!-- Create/Edit Modal -->
    <div v-if="showCreateDialog || showEditDialog" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full z-50">
      <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
        <div class="mt-3">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-medium text-gray-900">
              {{ showEditDialog ? 'Edit Book Loan' : 'Create New Book Loan' }}
            </h3>
            <button @click="closeDialog" class="text-gray-400 hover:text-gray-600">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>
          
          <form @submit.prevent="showEditDialog ? updateLoan() : createLoan()">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Student</label>
                <select v-model="form.student_id" required class="select">
                  <option value="">Select Student</option>
                  <option v-for="student in students" :key="student.id" :value="student.id">
                    {{ student.name }} ({{ student.student_id }})
                  </option>
                </select>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Book</label>
                <select v-model="form.book_id" required class="select">
                  <option value="">Select Book</option>
                  <option v-for="book in availableBooks" :key="book.id" :value="book.id">
                    {{ book.title }} by {{ book.author }} ({{ book.available_copies }} available)
                  </option>
                </select>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Due Date</label>
                <input 
                  type="datetime-local" 
                  v-model="form.due_date" 
                  required
                  class="input"
                />
              </div>
            </div>

            <div class="flex justify-end space-x-3 mt-6">
              <button type="button" @click="closeDialog" class="btn btn-secondary">
                Cancel
              </button>
              <button type="submit" class="btn btn-primary">
                {{ showEditDialog ? 'Update' : 'Create' }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

// State
const bookLoans = ref([])
const students = ref([])
const books = ref([])
const statistics = ref({
  total_loans: 0,
  active_loans: 0,
  overdue_loans: 0,
  returned_loans: 0
})
const loading = ref(false)
const error = ref('')
const showCreateDialog = ref(false)
const showEditDialog = ref(false)
const editingLoan = ref(null)

// Form data
const form = ref({
  student_id: '',
  book_id: '',
  due_date: ''
})

// Filters
const filters = ref({
  student_name: '',
  book_title: '',
  is_returned: ''
})

// Computed
const availableBooks = computed(() => {
  return books.value.filter(book => book.available_copies > 0)
})

// API Configuration
const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api'

// Methods
const loadBookLoans = async () => {
  loading.value = true
  error.value = ''
  
  try {
    const params = new URLSearchParams()
    if (filters.value.student_name) params.append('student_name', filters.value.student_name)
    if (filters.value.book_title) params.append('book_title', filters.value.book_title)
    if (filters.value.is_returned) params.append('is_returned', filters.value.is_returned)
    
    const response = await axios.get(`${API_BASE}/book-loans/?${params}`)
    bookLoans.value = response.data.results || response.data
  } catch (err) {
    error.value = 'Failed to load book loans: ' + err.message
  } finally {
    loading.value = false
  }
}

const loadStatistics = async () => {
  try {
    const response = await axios.get(`${API_BASE}/book-loans/statistics/`)
    statistics.value = response.data
  } catch (err) {
    console.error('Failed to load statistics:', err)
  }
}

const loadStudents = async () => {
  try {
    const response = await axios.get(`${API_BASE}/students/`)
    students.value = response.data.results || response.data
  } catch (err) {
    console.error('Failed to load students:', err)
  }
}

const loadBooks = async () => {
  try {
    const response = await axios.get(`${API_BASE}/books/`)
    books.value = response.data.results || response.data
  } catch (err) {
    console.error('Failed to load books:', err)
  }
}

const createLoan = async () => {
  try {
    await axios.post(`${API_BASE}/book-loans/`, form.value)
    closeDialog()
    await loadBookLoans()
    await loadStatistics()
    await loadBooks()
  } catch (err) {
    error.value = 'Failed to create loan: ' + err.message
  }
}

const updateLoan = async () => {
  try {
    await axios.patch(`${API_BASE}/book-loans/${editingLoan.value.id}/`, form.value)
    closeDialog()
    await loadBookLoans()
    await loadStatistics()
  } catch (err) {
    error.value = 'Failed to update loan: ' + err.message
  }
}

const deleteLoan = async (id) => {
  if (!confirm('Are you sure you want to delete this loan?')) return
  
  try {
    await axios.delete(`${API_BASE}/book-loans/${id}/`)
    await loadBookLoans()
    await loadStatistics()
    await loadBooks()
  } catch (err) {
    error.value = 'Failed to delete loan: ' + err.message
  }
}

const markAsReturned = async (id) => {
  try {
    await axios.post(`${API_BASE}/book-loans/${id}/mark_as_returned/`)
    await loadBookLoans()
    await loadStatistics()
    await loadBooks()
  } catch (err) {
    error.value = 'Failed to mark as returned: ' + err.message
  }
}

const editLoan = (loan) => {
  editingLoan.value = loan
  form.value = {
    student_id: loan.student.id,
    book_id: loan.book.id,
    due_date: formatDateForInput(loan.due_date)
  }
  showEditDialog.value = true
}

const closeDialog = () => {
  showCreateDialog.value = false
  showEditDialog.value = false
  editingLoan.value = null
  form.value = {
    student_id: '',
    book_id: '',
    due_date: ''
  }
  error.value = ''
}

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString()
}

const formatDateForInput = (dateString) => {
  return new Date(dateString).toISOString().slice(0, 16)
}

const isOverdue = (loan) => {
  return !loan.is_returned && new Date(loan.due_date) < new Date()
}

const getStatusText = (loan) => {
  if (loan.is_returned) return 'Returned'
  if (isOverdue(loan)) return 'Overdue'
  return 'Active'
}

const getStatusClasses = (loan) => {
  if (loan.is_returned) return 'bg-success-100 text-success-800'
  if (isOverdue(loan)) return 'bg-danger-100 text-danger-800'
  return 'bg-warning-100 text-warning-800'
}

// Lifecycle
onMounted(() => {
  loadBookLoans()
  loadStatistics()
  loadStudents()
  loadBooks()
})
</script>

<style scoped>
.admin-panel {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.header {
  margin-bottom: 30px;
}

.header h1 {
  color: #2c3e50;
  margin-bottom: 20px;
}

.stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 15px;
  margin-bottom: 20px;
}

.stat-card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  text-align: center;
  border-left: 4px solid #3498db;
}

.stat-card.active { border-left-color: #e74c3c; }
.stat-card.overdue { border-left-color: #f39c12; }
.stat-card.returned { border-left-color: #27ae60; }

.stat-card h3 {
  font-size: 24px;
  margin: 0 0 5px 0;
  color: #2c3e50;
}

.stat-card p {
  margin: 0;
  color: #7f8c8d;
  font-size: 14px;
}

.controls {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  gap: 20px;
}

.filters {
  display: flex;
  gap: 10px;
  flex: 1;
}

.filters input,
.filters select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.actions {
  display: flex;
  gap: 10px;
}

.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.2s;
}

.btn-primary {
  background-color: #3498db;
  color: white;
}

.btn-primary:hover {
  background-color: #2980b9;
}

.btn-secondary {
  background-color: #95a5a6;
  color: white;
}

.btn-secondary:hover {
  background-color: #7f8c8d;
}

.btn-success {
  background-color: #27ae60;
  color: white;
}

.btn-warning {
  background-color: #f39c12;
  color: white;
}

.btn-danger {
  background-color: #e74c3c;
  color: white;
}

.btn-sm {
  padding: 4px 8px;
  font-size: 12px;
}

.table-container {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  overflow: hidden;
}

.loans-table {
  width: 100%;
  border-collapse: collapse;
}

.loans-table th,
.loans-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.loans-table th {
  background-color: #f8f9fa;
  font-weight: 600;
  color: #2c3e50;
}

.loans-table tr:hover {
  background-color: #f8f9fa;
}

.loans-table tr.overdue {
  background-color: #fff3cd;
}

.status-active {
  color: #e74c3c;
  font-weight: 600;
}

.status-returned {
  color: #27ae60;
  font-weight: 600;
}

.status-overdue {
  color: #f39c12;
  font-weight: 600;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal {
  background: white;
  padding: 30px;
  border-radius: 8px;
  width: 90%;
  max-width: 500px;
  max-height: 80vh;
  overflow-y: auto;
}

.modal h2 {
  margin-top: 0;
  margin-bottom: 20px;
  color: #2c3e50;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: 600;
  color: #2c3e50;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.form-actions {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
  margin-top: 20px;
}

.loading {
  text-align: center;
  padding: 20px;
  color: #7f8c8d;
}

.error {
  background-color: #f8d7da;
  color: #721c24;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 20px;
}

@media (max-width: 768px) {
  .controls {
    flex-direction: column;
    align-items: stretch;
  }
  
  .filters {
    flex-direction: column;
  }
  
  .stats {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .loans-table {
    font-size: 12px;
  }
  
  .loans-table th,
  .loans-table td {
    padding: 8px 4px;
  }
}
</style>