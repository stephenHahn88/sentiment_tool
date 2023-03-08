def findDecision(obj): #obj[0]: t-1, obj[1]: t-2, obj[2]: t-3, obj[3]: anger, obj[4]: fear, obj[5]: sadness, obj[6]: none, obj[7]: irony, obj[8]: love, obj[9]: joy
	# {"feature": "t-1", "instances": 1370, "metric_value": 0.7355, "depth": 1}
	if obj[0] == 'V':
		# {"feature": "t-2", "instances": 361, "metric_value": 0.3977, "depth": 2}
		if obj[1] == 'i':
			# {"feature": "t-3", "instances": 111, "metric_value": 0.1931, "depth": 3}
			if obj[2] == 'V':
				# {"feature": "love", "instances": 60, "metric_value": 0.1576, "depth": 4}
				if obj[8]<=0.0:
					# {"feature": "fear", "instances": 59, "metric_value": 0.1464, "depth": 5}
					if obj[4]<=0.71:
						# {"feature": "anger", "instances": 49, "metric_value": 0.0755, "depth": 6}
						if obj[3]<=0.62:
							# {"feature": "sadness", "instances": 41, "metric_value": 0.0474, "depth": 7}
							if obj[5]>0.91:
								# {"feature": "none", "instances": 35, "metric_value": 0.0555, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 35, "metric_value": 0.0555, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 35, "metric_value": 0.0555, "depth": 10}
										if obj[9]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							elif obj[5]<=0.91:
								return 'i'
							else: return 'i'
						elif obj[3]>0.62:
							# {"feature": "sadness", "instances": 8, "metric_value": 0.2188, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 8, "metric_value": 0.2188, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 8, "metric_value": 0.2188, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 8, "metric_value": 0.2188, "depth": 10}
										if obj[9]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						else: return 'i'
					elif obj[4]>0.71:
						# {"feature": "anger", "instances": 10, "metric_value": 0.48, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "sadness", "instances": 10, "metric_value": 0.48, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 10, "metric_value": 0.48, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 10, "metric_value": 0.48, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 10, "metric_value": 0.48, "depth": 10}
										if obj[9]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						else: return 'i'
					else: return 'i'
				elif obj[8]>0.0:
					return 'I'
				else: return 'I'
			elif obj[2] == 'iv':
				return 'i'
			elif obj[2] == 'i':
				# {"feature": "anger", "instances": 8, "metric_value": 0.0, "depth": 4}
				if obj[3]<=0.13:
					return 'i'
				elif obj[3]>0.13:
					return 'I'
				else: return 'I'
			elif obj[2] == 'ii':
				return 'i'
			elif obj[2] == 'I':
				# {"feature": "sadness", "instances": 6, "metric_value": 0.4167, "depth": 4}
				if obj[5]<=0.0:
					# {"feature": "fear", "instances": 4, "metric_value": 0.3333, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "love", "instances": 3, "metric_value": 0.3333, "depth": 6}
						if obj[8]>0.0:
							# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[3]<=0.0:
								# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'ii'
										else: return 'ii'
									else: return 'ii'
								else: return 'ii'
							else: return 'ii'
						elif obj[8]<=0.0:
							return 'I'
						else: return 'I'
					elif obj[4]>0.0:
						return 'i'
					else: return 'i'
				elif obj[5]>0.0:
					return 'i'
				else: return 'i'
			elif obj[2] == 'START':
				# {"feature": "anger", "instances": 4, "metric_value": 0.3333, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "fear", "instances": 3, "metric_value": 0.4444, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 3, "metric_value": 0.4444, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						else: return 'i'
					else: return 'i'
				elif obj[3]>0.0:
					return 'i'
				else: return 'i'
			elif obj[2] == 'viio/ii':
				return 'i'
			elif obj[2] == 'bVI':
				# {"feature": "sadness", "instances": 4, "metric_value": 0.0, "depth": 4}
				if obj[5]<=0.51:
					return 'i'
				elif obj[5]>0.51:
					return 'bVI'
				else: return 'bVI'
			elif obj[2] == 'bIII':
				return 'i'
			elif obj[2] == 'iii':
				return 'V'
			elif obj[2] == 'v':
				return 'i'
			else: return 'i'
		elif obj[1] == 'I':
			# {"feature": "t-3", "instances": 107, "metric_value": 0.2532, "depth": 3}
			if obj[2] == 'V':
				# {"feature": "sadness", "instances": 63, "metric_value": 0.2058, "depth": 4}
				if obj[5]<=0.05:
					# {"feature": "fear", "instances": 62, "metric_value": 0.2014, "depth": 5}
					if obj[4]<=0.6:
						# {"feature": "love", "instances": 59, "metric_value": 0.1792, "depth": 6}
						if obj[8]>0.19:
							# {"feature": "joy", "instances": 35, "metric_value": 0.2381, "depth": 7}
							if obj[9]<=0.51:
								# {"feature": "anger", "instances": 33, "metric_value": 0.2222, "depth": 8}
								if obj[3]<=0.0:
									# {"feature": "none", "instances": 33, "metric_value": 0.2222, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 33, "metric_value": 0.2222, "depth": 10}
										if obj[7]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							elif obj[9]>0.51:
								# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[3]<=0.0:
									# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[7]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						elif obj[8]<=0.19:
							return 'I'
						else: return 'I'
					elif obj[4]>0.6:
						# {"feature": "anger", "instances": 3, "metric_value": 0.4444, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							else: return 'I'
						else: return 'I'
					else: return 'I'
				elif obj[5]>0.05:
					return 'iii'
				else: return 'iii'
			elif obj[2] == 'I':
				# {"feature": "love", "instances": 15, "metric_value": 0.3167, "depth": 4}
				if obj[8]>0.0:
					# {"feature": "anger", "instances": 8, "metric_value": 0.5938, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "fear", "instances": 8, "metric_value": 0.5938, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "sadness", "instances": 8, "metric_value": 0.5938, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 8, "metric_value": 0.5938, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 8, "metric_value": 0.5938, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 8, "metric_value": 0.5938, "depth": 10}
										if obj[9]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							else: return 'I'
						else: return 'I'
					else: return 'I'
				elif obj[8]<=0.0:
					return 'I'
				else: return 'I'
			elif obj[2] == 'IV':
				# {"feature": "sadness", "instances": 7, "metric_value": 0.1429, "depth": 4}
				if obj[5]<=0.0:
					return 'I'
				elif obj[5]>0.0:
					# {"feature": "love", "instances": 2, "metric_value": 0.0, "depth": 5}
					if obj[8]>0.0:
						return 'V'
					elif obj[8]<=0.0:
						return 'I'
					else: return 'I'
				else: return 'V'
			elif obj[2] == 'ii':
				# {"feature": "anger", "instances": 7, "metric_value": 0.2381, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "love", "instances": 6, "metric_value": 0.25, "depth": 5}
					if obj[8]>0.0:
						# {"feature": "fear", "instances": 4, "metric_value": 0.375, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "sadness", "instances": 4, "metric_value": 0.375, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 4, "metric_value": 0.375, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 4, "metric_value": 0.375, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[9]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							else: return 'I'
						else: return 'I'
					elif obj[8]<=0.0:
						return 'I'
					else: return 'I'
				elif obj[3]>0.0:
					return 'vi'
				else: return 'vi'
			elif obj[2] == 'vi':
				return 'I'
			elif obj[2] == 'i':
				# {"feature": "fear", "instances": 3, "metric_value": 0.0, "depth": 4}
				if obj[4]>0.0:
					return 'i'
				elif obj[4]<=0.0:
					return 'I'
				else: return 'I'
			elif obj[2] == 'START':
				return 'I'
			elif obj[2] == 'bVI':
				return 'I'
			elif obj[2] == 'bIII':
				return 'I'
			elif obj[2] == 'iv':
				return 'I'
			elif obj[2] == 'viio/ii':
				return 'I'
			elif obj[2] == 'iii':
				return 'I'
			else: return 'I'
		elif obj[1] == 'ii':
			# {"feature": "t-3", "instances": 67, "metric_value": 0.4442, "depth": 3}
			if obj[2] == 'V':
				# {"feature": "fear", "instances": 19, "metric_value": 0.5655, "depth": 4}
				if obj[4]<=0.65:
					# {"feature": "anger", "instances": 13, "metric_value": 0.5692, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "love", "instances": 10, "metric_value": 0.48, "depth": 6}
						if obj[8]>0.0:
							# {"feature": "joy", "instances": 5, "metric_value": 0.3, "depth": 7}
							if obj[9]<=0.0:
								# {"feature": "sadness", "instances": 4, "metric_value": 0.375, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "none", "instances": 4, "metric_value": 0.375, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[7]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							elif obj[9]>0.0:
								return 'I'
							else: return 'I'
						elif obj[8]<=0.0:
							# {"feature": "sadness", "instances": 5, "metric_value": 0.64, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 5, "metric_value": 0.64, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 5, "metric_value": 0.64, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 5, "metric_value": 0.64, "depth": 10}
										if obj[9]<=1.0:
											return 'ii'
										else: return 'ii'
									else: return 'ii'
								else: return 'ii'
							else: return 'ii'
						else: return 'ii'
					elif obj[3]>0.0:
						# {"feature": "joy", "instances": 3, "metric_value": 0.3333, "depth": 6}
						if obj[9]<=0.0:
							# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						elif obj[9]>0.0:
							return 'i'
						else: return 'i'
					else: return 'i'
				elif obj[4]>0.65:
					# {"feature": "anger", "instances": 6, "metric_value": 0.2778, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "sadness", "instances": 6, "metric_value": 0.2778, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 6, "metric_value": 0.2778, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 6, "metric_value": 0.2778, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 6, "metric_value": 0.2778, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 6, "metric_value": 0.2778, "depth": 10}
										if obj[9]<=0.0:
											return 'ii'
										else: return 'ii'
									else: return 'ii'
								else: return 'ii'
							else: return 'ii'
						else: return 'ii'
					else: return 'ii'
				else: return 'ii'
			elif obj[2] == 'i':
				# {"feature": "love", "instances": 15, "metric_value": 0.5333, "depth": 4}
				if obj[8]<=0.0:
					# {"feature": "joy", "instances": 14, "metric_value": 0.4835, "depth": 5}
					if obj[9]<=0.0:
						# {"feature": "fear", "instances": 13, "metric_value": 0.4718, "depth": 6}
						if obj[4]<=0.5:
							# {"feature": "anger", "instances": 10, "metric_value": 0.45, "depth": 7}
							if obj[3]>0.0:
								# {"feature": "sadness", "instances": 6, "metric_value": 0.25, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "none", "instances": 4, "metric_value": 0.375, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[7]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								elif obj[5]>0.0:
									return 'V'
								else: return 'V'
							elif obj[3]<=0.0:
								# {"feature": "sadness", "instances": 4, "metric_value": 0.375, "depth": 8}
								if obj[5]<=1.0:
									# {"feature": "none", "instances": 4, "metric_value": 0.375, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[7]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						elif obj[4]>0.5:
							# {"feature": "anger", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[3]<=0.0:
								# {"feature": "sadness", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[7]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						else: return 'i'
					elif obj[9]>0.0:
						return 'I'
					else: return 'I'
				elif obj[8]>0.0:
					return 'I'
				else: return 'I'
			elif obj[2] == 'vi':
				# {"feature": "joy", "instances": 13, "metric_value": 0.1026, "depth": 4}
				if obj[9]<=0.0:
					return 'I'
				elif obj[9]>0.0:
					# {"feature": "love", "instances": 3, "metric_value": 0.0, "depth": 5}
					if obj[8]<=0.0:
						return 'I'
					elif obj[8]>0.0:
						return 'iii'
					else: return 'iii'
				else: return 'I'
			elif obj[2] == 'I':
				# {"feature": "sadness", "instances": 8, "metric_value": 0.2143, "depth": 4}
				if obj[5]<=0.0:
					# {"feature": "love", "instances": 7, "metric_value": 0.2143, "depth": 5}
					if obj[8]>0.0:
						# {"feature": "anger", "instances": 4, "metric_value": 0.375, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "fear", "instances": 4, "metric_value": 0.375, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "none", "instances": 4, "metric_value": 0.375, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 4, "metric_value": 0.375, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[9]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							else: return 'I'
						else: return 'I'
					elif obj[8]<=0.0:
						return 'I'
					else: return 'I'
				elif obj[5]>0.0:
					return 'i'
				else: return 'i'
			elif obj[2] == 'iii':
				# {"feature": "anger", "instances": 3, "metric_value": 0.0, "depth": 4}
				if obj[3]<=0.0:
					return 'I'
				elif obj[3]>0.0:
					return 'i'
				else: return 'i'
			elif obj[2] == 'IV':
				return 'I'
			elif obj[2] == 'vii':
				return 'i'
			elif obj[2] == 'bVI':
				return 'bVI'
			elif obj[2] == 'v':
				# {"feature": "anger", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[3]>0.0:
					return 'i'
				elif obj[3]<=0.0:
					return 'I'
				else: return 'I'
			elif obj[2] == 'bIII':
				return 'V'
			else: return 'V'
		elif obj[1] == 'V':
			# {"feature": "t-3", "instances": 18, "metric_value": 0.3673, "depth": 3}
			if obj[2] == 'ii':
				# {"feature": "fear", "instances": 9, "metric_value": 0.3444, "depth": 4}
				if obj[4]<=0.0:
					# {"feature": "sadness", "instances": 5, "metric_value": 0.0, "depth": 5}
					if obj[5]<=0.0:
						return 'ii'
					elif obj[5]>0.0:
						return 'i'
					else: return 'i'
				elif obj[4]>0.0:
					# {"feature": "anger", "instances": 4, "metric_value": 0.0, "depth": 5}
					if obj[3]>0.0:
						return 'I'
					elif obj[3]<=0.0:
						return 'ii'
					else: return 'ii'
				else: return 'I'
			elif obj[2] == 'I':
				return 'I'
			elif obj[2] == 'i':
				# {"feature": "fear", "instances": 4, "metric_value": 0.25, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						else: return 'i'
					else: return 'i'
				elif obj[4]<=0.0:
					return 'i'
				else: return 'i'
			elif obj[2] == 'bIII':
				return 'I'
			else: return 'I'
		elif obj[1] == 'bVI':
			# {"feature": "t-3", "instances": 11, "metric_value": 0.2857, "depth": 3}
			if obj[2] == 'V':
				# {"feature": "love", "instances": 7, "metric_value": 0.2381, "depth": 4}
				if obj[8]<=0.0:
					# {"feature": "anger", "instances": 6, "metric_value": 0.2222, "depth": 5}
					if obj[3]<=0.5:
						# {"feature": "sadness", "instances": 3, "metric_value": 0.0, "depth": 6}
						if obj[5]>0.5:
							return 'bVI'
						elif obj[5]<=0.5:
							return 'viio/V'
						else: return 'viio/V'
					elif obj[3]>0.5:
						return 'bVI'
					else: return 'bVI'
				elif obj[8]>0.0:
					return 'I'
				else: return 'I'
			elif obj[2] == 'viio/ii':
				return 'bVI'
			elif obj[2] == 'I':
				return 'bVI'
			elif obj[2] == 'viio/V':
				return 'i'
			else: return 'i'
		elif obj[1] == 'iv':
			# {"feature": "t-3", "instances": 9, "metric_value": 0.3111, "depth": 3}
			if obj[2] == 'I':
				# {"feature": "fear", "instances": 5, "metric_value": 0.4, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "sadness", "instances": 3, "metric_value": 0.3333, "depth": 5}
					if obj[5]<=0.0:
						# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						else: return 'i'
					elif obj[5]>0.0:
						return 'bVI'
					else: return 'bVI'
				elif obj[4]<=0.0:
					return 'i'
				else: return 'i'
			elif obj[2] == 'iii':
				return 'ii'
			elif obj[2] == 'bvii':
				return 'vii'
			elif obj[2] == 'i':
				return 'i'
			elif obj[2] == 'IV':
				return 'I'
			else: return 'I'
		elif obj[1] == 'bIII':
			# {"feature": "t-3", "instances": 6, "metric_value": 0.1667, "depth": 3}
			if obj[2] == 'iv':
				return 'I'
			elif obj[2] == 'i':
				return 'I'
			elif obj[2] == 'bVII':
				# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "fear", "instances": 2, "metric_value": 0.5, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'bVII'
										else: return 'bVII'
									else: return 'bVII'
								else: return 'bVII'
							else: return 'bVII'
						else: return 'bVII'
					else: return 'bVII'
				else: return 'bVII'
			else: return 'bVII'
		elif obj[1] == 'vi':
			# {"feature": "t-3", "instances": 6, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'iii':
				return 'I'
			elif obj[2] == 'I':
				return 'i'
			elif obj[2] == 'V':
				return 'I'
			elif obj[2] == 'IV':
				return 'I'
			else: return 'I'
		elif obj[1] == 'viio/V':
			# {"feature": "t-3", "instances": 6, "metric_value": 0.1667, "depth": 3}
			if obj[2] == 'V':
				# {"feature": "anger", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[3]<=0.5:
					return 'IV'
				elif obj[3]>0.5:
					return 'i'
				else: return 'i'
			elif obj[2] == 'i':
				return 'I'
			elif obj[2] == 'bVI':
				return 'i'
			elif obj[2] == 'iv':
				return 'i'
			else: return 'i'
		elif obj[1] == 'iii':
			# {"feature": "t-3", "instances": 6, "metric_value": 0.1667, "depth": 3}
			if obj[2] == 'V':
				return 'I'
			elif obj[2] == 'vii':
				# {"feature": "fear", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[4]<=0.0:
					return 'vi'
				elif obj[4]>0.0:
					return 'i'
				else: return 'i'
			elif obj[2] == 'bVI':
				return 'I'
			else: return 'I'
		elif obj[1] == 'v':
			return 'i'
		elif obj[1] == 'IV':
			# {"feature": "t-3", "instances": 3, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'vi':
				return 'bVI'
			elif obj[2] == 'I':
				return 'I'
			elif obj[2] == 'V':
				return 'ii'
			else: return 'ii'
		elif obj[1] == 'bVII':
			return 'bVI'
		elif obj[1] == 'viio/ii':
			# {"feature": "t-3", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'iii':
				return 'I'
			elif obj[2] == 'bVI':
				return 'bVI'
			else: return 'bVI'
		elif obj[1] == 'vii':
			return 'i'
		elif obj[1] == 'START':
			# {"feature": "anger", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[3]<=0.0:
				return 'ii'
			elif obj[3]>0.0:
				return 'i'
			else: return 'i'
		else: return 'ii'
	elif obj[0] == 'I':
		# {"feature": "t-2", "instances": 250, "metric_value": 0.6985, "depth": 2}
		if obj[1] == 'V':
			# {"feature": "t-3", "instances": 140, "metric_value": 0.7015, "depth": 3}
			if obj[2] == 'I':
				# {"feature": "fear", "instances": 83, "metric_value": 0.6752, "depth": 4}
				if obj[4]<=0.5:
					# {"feature": "anger", "instances": 76, "metric_value": 0.6408, "depth": 5}
					if obj[3]<=0.67:
						# {"feature": "sadness", "instances": 73, "metric_value": 0.6309, "depth": 6}
						if obj[5]<=0.5:
							# {"feature": "joy", "instances": 72, "metric_value": 0.6289, "depth": 7}
							if obj[9]<=0.33:
								# {"feature": "love", "instances": 36, "metric_value": 0.6863, "depth": 8}
								if obj[8]>0.04:
									# {"feature": "none", "instances": 34, "metric_value": 0.6972, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 34, "metric_value": 0.6972, "depth": 10}
										if obj[7]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								elif obj[8]<=0.04:
									# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[7]<=0.0:
											return 'bVI'
										else: return 'bVI'
									else: return 'bVI'
								else: return 'bVI'
							elif obj[9]>0.33:
								# {"feature": "love", "instances": 36, "metric_value": 0.5253, "depth": 8}
								if obj[8]<=0.43:
									# {"feature": "none", "instances": 33, "metric_value": 0.5124, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 33, "metric_value": 0.5124, "depth": 10}
										if obj[7]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								elif obj[8]>0.43:
									# {"feature": "none", "instances": 3, "metric_value": 0.6667, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 3, "metric_value": 0.6667, "depth": 10}
										if obj[7]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							else: return 'V'
						elif obj[5]>0.5:
							return 'i'
						else: return 'i'
					elif obj[3]>0.67:
						# {"feature": "love", "instances": 3, "metric_value": 0.0, "depth": 6}
						if obj[8]>0.0:
							return 'vi'
						elif obj[8]<=0.0:
							return 'iii'
						else: return 'iii'
					else: return 'vi'
				elif obj[4]>0.5:
					# {"feature": "joy", "instances": 7, "metric_value": 0.5714, "depth": 5}
					if obj[9]<=0.0:
						# {"feature": "love", "instances": 6, "metric_value": 0.5556, "depth": 6}
						if obj[8]<=0.0:
							# {"feature": "anger", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[3]<=0.0:
								# {"feature": "sadness", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[7]<=0.0:
											return 'IV'
										else: return 'IV'
									else: return 'IV'
								else: return 'IV'
							else: return 'IV'
						elif obj[8]>0.0:
							# {"feature": "anger", "instances": 3, "metric_value": 0.6667, "depth": 7}
							if obj[3]<=0.0:
								# {"feature": "sadness", "instances": 3, "metric_value": 0.6667, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "none", "instances": 3, "metric_value": 0.6667, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 3, "metric_value": 0.6667, "depth": 10}
										if obj[7]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						else: return 'i'
					elif obj[9]>0.0:
						return 'i'
					else: return 'i'
				else: return 'IV'
			elif obj[2] == 'ii':
				# {"feature": "fear", "instances": 27, "metric_value": 0.7793, "depth": 4}
				if obj[4]<=0.78:
					# {"feature": "joy", "instances": 25, "metric_value": 0.7756, "depth": 5}
					if obj[9]<=0.82:
						# {"feature": "sadness", "instances": 16, "metric_value": 0.7143, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "love", "instances": 14, "metric_value": 0.7013, "depth": 7}
							if obj[8]>0.33:
								# {"feature": "anger", "instances": 11, "metric_value": 0.7107, "depth": 8}
								if obj[3]<=0.0:
									# {"feature": "none", "instances": 11, "metric_value": 0.7107, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 11, "metric_value": 0.7107, "depth": 10}
										if obj[7]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							elif obj[8]<=0.33:
								# {"feature": "anger", "instances": 3, "metric_value": 0.6667, "depth": 8}
								if obj[3]<=0.0:
									# {"feature": "none", "instances": 3, "metric_value": 0.6667, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 3, "metric_value": 0.6667, "depth": 10}
										if obj[7]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						elif obj[5]>0.0:
							# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[3]<=0.0:
								# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0.0:
											return 'ii'
										else: return 'ii'
									else: return 'ii'
								else: return 'ii'
							else: return 'ii'
						else: return 'ii'
					elif obj[9]>0.82:
						# {"feature": "anger", "instances": 9, "metric_value": 0.7654, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "sadness", "instances": 9, "metric_value": 0.7654, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 9, "metric_value": 0.7654, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 9, "metric_value": 0.7654, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "love", "instances": 9, "metric_value": 0.7654, "depth": 10}
										if obj[8]<=0.0:
											return 'IV'
										else: return 'IV'
									else: return 'IV'
								else: return 'IV'
							else: return 'IV'
						else: return 'IV'
					else: return 'IV'
				elif obj[4]>0.78:
					return 'I'
				else: return 'I'
			elif obj[2] == 'V':
				# {"feature": "joy", "instances": 9, "metric_value": 0.6667, "depth": 4}
				if obj[9]<=0.0:
					# {"feature": "fear", "instances": 6, "metric_value": 0.4667, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "anger", "instances": 5, "metric_value": 0.5, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "sadness", "instances": 4, "metric_value": 0.625, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 4, "metric_value": 0.625, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 4, "metric_value": 0.625, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "love", "instances": 4, "metric_value": 0.625, "depth": 10}
										if obj[8]<=1.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						elif obj[3]>0.0:
							return 'V'
						else: return 'V'
					elif obj[4]>0.0:
						return 'IV'
					else: return 'IV'
				elif obj[9]>0.0:
					# {"feature": "anger", "instances": 3, "metric_value": 0.3333, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "love", "instances": 2, "metric_value": 0.0, "depth": 6}
						if obj[8]>0.5:
							return 'iii'
						elif obj[8]<=0.5:
							return 'viio/ii'
						else: return 'viio/ii'
					elif obj[3]>0.0:
						return 'vii'
					else: return 'vii'
				else: return 'iii'
			elif obj[2] == 'bIII':
				# {"feature": "fear", "instances": 5, "metric_value": 0.2667, "depth": 4}
				if obj[4]<=0.0:
					# {"feature": "sadness", "instances": 3, "metric_value": 0.0, "depth": 5}
					if obj[5]>0.0:
						return 'vi'
					elif obj[5]<=0.0:
						return 'V'
					else: return 'V'
				elif obj[4]>0.0:
					return 'iii'
				else: return 'iii'
			elif obj[2] == 'vi':
				# {"feature": "love", "instances": 4, "metric_value": 0.3333, "depth": 4}
				if obj[8]<=0.0:
					# {"feature": "fear", "instances": 3, "metric_value": 0.3333, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "joy", "instances": 2, "metric_value": 0.0, "depth": 6}
						if obj[9]<=0.0:
							return 'V'
						elif obj[9]>0.0:
							return 'iii'
						else: return 'iii'
					elif obj[4]<=0.0:
						return 'V'
					else: return 'V'
				elif obj[8]>0.0:
					return 'I'
				else: return 'I'
			elif obj[2] == 'iii':
				# {"feature": "fear", "instances": 4, "metric_value": 0.0, "depth": 4}
				if obj[4]<=0.0:
					return 'V'
				elif obj[4]>0.0:
					return 'I'
				else: return 'I'
			elif obj[2] == 'i':
				# {"feature": "sadness", "instances": 3, "metric_value": 0.0, "depth": 4}
				if obj[5]>0.0:
					return 'iv'
				elif obj[5]<=0.0:
					return 'I'
				else: return 'I'
			elif obj[2] == 'iv':
				return 'IV'
			elif obj[2] == 'bVI':
				# {"feature": "love", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[8]<=0.0:
					return 'IV'
				elif obj[8]>0.0:
					return 'V'
				else: return 'V'
			elif obj[2] == 'viio/V':
				return 'V'
			else: return 'V'
		elif obj[1] == 'IV':
			# {"feature": "t-3", "instances": 27, "metric_value": 0.6229, "depth": 3}
			if obj[2] == 'I':
				# {"feature": "joy", "instances": 22, "metric_value": 0.6723, "depth": 4}
				if obj[9]<=0.01:
					# {"feature": "sadness", "instances": 16, "metric_value": 0.6167, "depth": 5}
					if obj[5]<=0.51:
						# {"feature": "love", "instances": 15, "metric_value": 0.6154, "depth": 6}
						if obj[8]>0.99:
							# {"feature": "anger", "instances": 13, "metric_value": 0.7101, "depth": 7}
							if obj[3]<=0.0:
								# {"feature": "fear", "instances": 13, "metric_value": 0.7101, "depth": 8}
								if obj[4]<=0.0:
									# {"feature": "none", "instances": 13, "metric_value": 0.7101, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 13, "metric_value": 0.7101, "depth": 10}
										if obj[7]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						elif obj[8]<=0.99:
							return 'V'
						else: return 'V'
					elif obj[5]>0.51:
						return 'iii'
					else: return 'iii'
				elif obj[9]>0.01:
					# {"feature": "love", "instances": 6, "metric_value": 0.4167, "depth": 5}
					if obj[8]<=0.0:
						# {"feature": "anger", "instances": 4, "metric_value": 0.625, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "fear", "instances": 4, "metric_value": 0.625, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "sadness", "instances": 4, "metric_value": 0.625, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "none", "instances": 4, "metric_value": 0.625, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 4, "metric_value": 0.625, "depth": 10}
										if obj[7]<=0.0:
											return 'ii'
										else: return 'ii'
									else: return 'ii'
								else: return 'ii'
							else: return 'ii'
						else: return 'ii'
					elif obj[8]>0.0:
						return 'IV'
					else: return 'IV'
				else: return 'IV'
			elif obj[2] == 'vi':
				return 'V'
			elif obj[2] == 'ii':
				return 'V'
			elif obj[2] == 'IV':
				return 'IV'
			elif obj[2] == 'iii':
				return 'V'
			elif obj[2] == 'V':
				return 'I'
			else: return 'I'
		elif obj[1] == 'I':
			# {"feature": "t-3", "instances": 25, "metric_value": 0.52, "depth": 3}
			if obj[2] == 'V':
				# {"feature": "anger", "instances": 17, "metric_value": 0.6324, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "love", "instances": 16, "metric_value": 0.6151, "depth": 5}
					if obj[8]<=0.58:
						# {"feature": "fear", "instances": 9, "metric_value": 0.5556, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "sadness", "instances": 6, "metric_value": 0.4667, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 5, "metric_value": 0.56, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 5, "metric_value": 0.56, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 5, "metric_value": 0.56, "depth": 10}
										if obj[9]<=1.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							elif obj[5]>0.0:
								return 'V'
							else: return 'V'
						elif obj[4]>0.0:
							# {"feature": "joy", "instances": 3, "metric_value": 0.3333, "depth": 7}
							if obj[9]<=0.0:
								# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[7]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							elif obj[9]>0.0:
								return 'IV'
							else: return 'IV'
						else: return 'V'
					elif obj[8]>0.58:
						# {"feature": "fear", "instances": 7, "metric_value": 0.6122, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "sadness", "instances": 7, "metric_value": 0.6122, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 7, "metric_value": 0.6122, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 7, "metric_value": 0.6122, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 7, "metric_value": 0.6122, "depth": 10}
										if obj[9]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						else: return 'V'
					else: return 'V'
				elif obj[3]>0.0:
					return 'iii'
				else: return 'iii'
			elif obj[2] == 'IV':
				# {"feature": "love", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[8]<=0.0:
					return 'V'
				elif obj[8]>0.0:
					return 'IV'
				else: return 'IV'
			elif obj[2] == 'i':
				return 'IV'
			elif obj[2] == 'ii':
				return 'I'
			elif obj[2] == 'v':
				return 'IV'
			elif obj[2] == 'I':
				return 'IV'
			elif obj[2] == 'vi':
				return 'IV'
			else: return 'IV'
		elif obj[1] == 'i':
			# {"feature": "joy", "instances": 19, "metric_value": 0.397, "depth": 3}
			if obj[9]<=0.0:
				# {"feature": "love", "instances": 14, "metric_value": 0.2024, "depth": 4}
				if obj[8]<=0.0:
					# {"feature": "t-3", "instances": 12, "metric_value": 0.1111, "depth": 5}
					if obj[2] == 'V':
						return 'iv'
					elif obj[2] == 'vii':
						# {"feature": "anger", "instances": 3, "metric_value": 0.0, "depth": 6}
						if obj[3]>0.0:
							return 'iv'
						elif obj[3]<=0.0:
							return 'V'
						else: return 'V'
					else: return 'iv'
				elif obj[8]>0.0:
					# {"feature": "t-3", "instances": 2, "metric_value": 0.5, "depth": 5}
					if obj[2] == 'V':
						# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "fear", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[7]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							else: return 'I'
						else: return 'I'
					else: return 'I'
				else: return 'I'
			elif obj[9]>0.0:
				# {"feature": "sadness", "instances": 5, "metric_value": 0.0, "depth": 4}
				if obj[5]>0.0:
					return 'IV'
				elif obj[5]<=0.0:
					return 'I'
				else: return 'I'
			else: return 'IV'
		elif obj[1] == 'ii':
			# {"feature": "t-3", "instances": 8, "metric_value": 0.3125, "depth": 3}
			if obj[2] == 'vi':
				# {"feature": "anger", "instances": 4, "metric_value": 0.375, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "fear", "instances": 4, "metric_value": 0.375, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 4, "metric_value": 0.375, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 4, "metric_value": 0.375, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 4, "metric_value": 0.375, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 4, "metric_value": 0.375, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "joy", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[9]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						else: return 'V'
					else: return 'V'
				else: return 'V'
			elif obj[2] == 'ii':
				# {"feature": "anger", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[3]<=0.0:
					return 'vi'
				elif obj[3]>0.0:
					return 'V'
				else: return 'V'
			elif obj[2] == 'I':
				return 'V'
			elif obj[2] == 'IV':
				return 'V'
			else: return 'V'
		elif obj[1] == 'iv':
			# {"feature": "t-3", "instances": 7, "metric_value": 0.3571, "depth": 3}
			if obj[2] == 'I':
				# {"feature": "fear", "instances": 4, "metric_value": 0.25, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "joy", "instances": 2, "metric_value": 0.0, "depth": 5}
					if obj[9]>0.0:
						return 'bVI'
					elif obj[9]<=0.0:
						return 'bIII'
					else: return 'bIII'
				elif obj[4]<=0.0:
					return 'V'
				else: return 'V'
			elif obj[2] == 'bVI':
				return 'IV'
			elif obj[2] == 'IV':
				return 'V'
			elif obj[2] == 'vi':
				return 'iv'
			else: return 'iv'
		elif obj[1] == 'vi':
			# {"feature": "t-3", "instances": 6, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'iii':
				return 'V'
			elif obj[2] == 'V':
				return 'i'
			elif obj[2] == 'ii':
				return 'I'
			else: return 'I'
		elif obj[1] == 'bVI':
			# {"feature": "love", "instances": 4, "metric_value": 0.25, "depth": 3}
			if obj[8]<=0.5:
				return 'V'
			elif obj[8]>0.5:
				# {"feature": "t-3", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[2] == 'bVI':
					return 'IV'
				elif obj[2] == 'bIII':
					return 'iv'
				else: return 'iv'
			else: return 'IV'
		elif obj[1] == 'START':
			# {"feature": "love", "instances": 4, "metric_value": 0.25, "depth": 3}
			if obj[8]<=0.5:
				return 'V'
			elif obj[8]>0.5:
				# {"feature": "t-3", "instances": 2, "metric_value": 0.5, "depth": 4}
				if obj[2] == 'PAD':
					# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "fear", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'iii'
										else: return 'iii'
									else: return 'iii'
								else: return 'iii'
							else: return 'iii'
						else: return 'iii'
					else: return 'iii'
				else: return 'iii'
			else: return 'iii'
		elif obj[1] == 'bvii':
			return 'bvii'
		elif obj[1] == 'v':
			# {"feature": "t-3", "instances": 3, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'v':
				return 'iv'
			elif obj[2] == 'bVII':
				return 'I'
			else: return 'I'
		elif obj[1] == 'bIII':
			return 'V'
		elif obj[1] == 'iii':
			return 'V'
		elif obj[1] == 'vii':
			return 'vi'
		else: return 'vi'
	elif obj[0] == 'i':
		# {"feature": "t-3", "instances": 218, "metric_value": 0.6476, "depth": 2}
		if obj[2] == 'i':
			# {"feature": "t-2", "instances": 111, "metric_value": 0.6284, "depth": 3}
			if obj[1] == 'V':
				# {"feature": "love", "instances": 87, "metric_value": 0.6235, "depth": 4}
				if obj[8]<=0.0:
					# {"feature": "joy", "instances": 81, "metric_value": 0.5758, "depth": 5}
					if obj[9]<=0.0:
						# {"feature": "fear", "instances": 78, "metric_value": 0.5631, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "anger", "instances": 55, "metric_value": 0.4909, "depth": 7}
							if obj[3]<=0.0:
								# {"feature": "sadness", "instances": 45, "metric_value": 0.4711, "depth": 8}
								if obj[5]<=1.0:
									# {"feature": "none", "instances": 45, "metric_value": 0.4711, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 45, "metric_value": 0.4711, "depth": 10}
										if obj[7]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							elif obj[3]>0.0:
								# {"feature": "sadness", "instances": 10, "metric_value": 0.525, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "none", "instances": 8, "metric_value": 0.5312, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 8, "metric_value": 0.5312, "depth": 10}
										if obj[7]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								elif obj[5]>0.0:
									# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[7]<=0.0:
											return 'iv'
										else: return 'iv'
									else: return 'iv'
								else: return 'iv'
							else: return 'V'
						elif obj[4]>0.0:
							# {"feature": "sadness", "instances": 23, "metric_value": 0.6334, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "anger", "instances": 17, "metric_value": 0.5255, "depth": 8}
								if obj[3]<=0.0:
									# {"feature": "none", "instances": 15, "metric_value": 0.5956, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 15, "metric_value": 0.5956, "depth": 10}
										if obj[7]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								elif obj[3]>0.0:
									return 'ii'
								else: return 'ii'
							elif obj[5]>0.0:
								# {"feature": "anger", "instances": 6, "metric_value": 0.5333, "depth": 8}
								if obj[3]<=0.0:
									# {"feature": "none", "instances": 5, "metric_value": 0.64, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 5, "metric_value": 0.64, "depth": 10}
										if obj[7]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								elif obj[3]>0.0:
									return 'bIII'
								else: return 'bIII'
							else: return 'i'
						else: return 'V'
					elif obj[9]>0.0:
						return 'I'
					else: return 'I'
				elif obj[8]>0.0:
					# {"feature": "sadness", "instances": 6, "metric_value": 0.4167, "depth": 5}
					if obj[5]<=0.5:
						# {"feature": "anger", "instances": 4, "metric_value": 0.25, "depth": 6}
						if obj[3]>0.0:
							return 'bVI'
						elif obj[3]<=0.0:
							# {"feature": "fear", "instances": 2, "metric_value": 0.0, "depth": 7}
							if obj[4]>0.0:
								return 'bVI'
							elif obj[4]<=0.0:
								return 'I'
							else: return 'I'
						else: return 'bVI'
					elif obj[5]>0.5:
						# {"feature": "fear", "instances": 2, "metric_value": 0.0, "depth": 6}
						if obj[4]>0.0:
							return 'i'
						elif obj[4]<=0.0:
							return 'bIII'
						else: return 'bIII'
					else: return 'i'
				else: return 'bVI'
			elif obj[1] == 'ii':
				# {"feature": "fear", "instances": 9, "metric_value": 0.3333, "depth": 4}
				if obj[4]<=0.0:
					# {"feature": "anger", "instances": 6, "metric_value": 0.2667, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "sadness", "instances": 5, "metric_value": 0.32, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "none", "instances": 5, "metric_value": 0.32, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 5, "metric_value": 0.32, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 5, "metric_value": 0.32, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[9]<=0.0:
											return 'ii'
										else: return 'ii'
									else: return 'ii'
								else: return 'ii'
							else: return 'ii'
						else: return 'ii'
					elif obj[3]>0.0:
						return 'ii'
					else: return 'ii'
				elif obj[4]>0.0:
					# {"feature": "sadness", "instances": 3, "metric_value": 0.0, "depth": 5}
					if obj[5]>0.0:
						return 'viio/ii'
					elif obj[5]<=0.0:
						return 'V'
					else: return 'V'
				else: return 'viio/ii'
			elif obj[1] == 'iv':
				# {"feature": "anger", "instances": 7, "metric_value": 0.3571, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "joy", "instances": 4, "metric_value": 0.3333, "depth": 5}
					if obj[9]<=0.0:
						# {"feature": "fear", "instances": 3, "metric_value": 0.3333, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						elif obj[4]>0.0:
							return 'ii'
						else: return 'ii'
					elif obj[9]>0.0:
						return 'bIII'
					else: return 'bIII'
				elif obj[3]>0.0:
					return 'V'
				else: return 'V'
			elif obj[1] == 'vii':
				# {"feature": "anger", "instances": 3, "metric_value": 0.3333, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "fear", "instances": 2, "metric_value": 0.0, "depth": 5}
					if obj[4]<=0.0:
						return 'I'
					elif obj[4]>0.0:
						return 'vii'
					else: return 'vii'
				elif obj[3]<=0.0:
					return 'I'
				else: return 'I'
			elif obj[1] == 'viio/ii':
				# {"feature": "fear", "instances": 3, "metric_value": 0.0, "depth": 4}
				if obj[4]<=0.0:
					return 'ii'
				elif obj[4]>0.0:
					return 'V'
				else: return 'V'
			elif obj[1] == 'i':
				return 'V'
			else: return 'V'
		elif obj[2] == 'V':
			# {"feature": "t-2", "instances": 22, "metric_value": 0.5326, "depth": 3}
			if obj[1] == 'i':
				# {"feature": "sadness", "instances": 8, "metric_value": 0.4583, "depth": 4}
				if obj[5]>0.5:
					# {"feature": "anger", "instances": 6, "metric_value": 0.2667, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "fear", "instances": 5, "metric_value": 0.3, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "none", "instances": 4, "metric_value": 0.375, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 4, "metric_value": 0.375, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 4, "metric_value": 0.375, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[9]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						elif obj[4]>0.0:
							return 'V'
						else: return 'V'
					elif obj[3]>0.0:
						return 'i'
					else: return 'i'
				elif obj[5]<=0.5:
					# {"feature": "fear", "instances": 2, "metric_value": 0.0, "depth": 5}
					if obj[4]>0.0:
						return 'ii'
					elif obj[4]<=0.0:
						return 'iv'
					else: return 'iv'
				else: return 'ii'
			elif obj[1] == 'I':
				# {"feature": "fear", "instances": 6, "metric_value": 0.4167, "depth": 4}
				if obj[4]<=0.8:
					# {"feature": "sadness", "instances": 4, "metric_value": 0.25, "depth": 5}
					if obj[5]>0.2:
						# {"feature": "love", "instances": 2, "metric_value": 0.0, "depth": 6}
						if obj[8]>0.0:
							return 'V'
						elif obj[8]<=0.0:
							return 'v'
						else: return 'v'
					elif obj[5]<=0.2:
						return 'iv'
					else: return 'iv'
				elif obj[4]>0.8:
					return 'V'
				else: return 'V'
			elif obj[1] == 'V':
				# {"feature": "anger", "instances": 5, "metric_value": 0.3, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "fear", "instances": 4, "metric_value": 0.3333, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 3, "metric_value": 0.4444, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						else: return 'V'
					elif obj[4]>0.0:
						return 'V'
					else: return 'V'
				elif obj[3]>0.0:
					return 'iii'
				else: return 'iii'
			elif obj[1] == 'bVI':
				return 'V'
			elif obj[1] == 'v':
				return 'V'
			elif obj[1] == 'iv':
				return 'V'
			else: return 'V'
		elif obj[2] == 'ii':
			# {"feature": "anger", "instances": 18, "metric_value": 0.7341, "depth": 3}
			if obj[3]<=0.71:
				# {"feature": "t-2", "instances": 14, "metric_value": 0.6786, "depth": 4}
				if obj[1] == 'V':
					# {"feature": "fear", "instances": 12, "metric_value": 0.7048, "depth": 5}
					if obj[4]<=0.5:
						# {"feature": "sadness", "instances": 7, "metric_value": 0.5429, "depth": 6}
						if obj[5]<=0.48:
							# {"feature": "love", "instances": 5, "metric_value": 0.4667, "depth": 7}
							if obj[8]<=0.0:
								# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							elif obj[8]>0.0:
								# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'bVI'
										else: return 'bVI'
									else: return 'bVI'
								else: return 'bVI'
							else: return 'bVI'
						elif obj[5]>0.48:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						else: return 'i'
					elif obj[4]>0.5:
						# {"feature": "sadness", "instances": 5, "metric_value": 0.5, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 4, "metric_value": 0.625, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 4, "metric_value": 0.625, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 4, "metric_value": 0.625, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 4, "metric_value": 0.625, "depth": 10}
										if obj[9]<=0.0:
											return 'vii'
										else: return 'vii'
									else: return 'vii'
								else: return 'vii'
							else: return 'vii'
						elif obj[5]>0.0:
							return 'V'
						else: return 'V'
					else: return 'vii'
				elif obj[1] == 'bIII':
					return 'ii'
				elif obj[1] == 'ii':
					return 'bIII'
				else: return 'bIII'
			elif obj[3]>0.71:
				# {"feature": "t-2", "instances": 4, "metric_value": 0.375, "depth": 4}
				if obj[1] == 'V':
					# {"feature": "fear", "instances": 4, "metric_value": 0.375, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 4, "metric_value": 0.375, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 4, "metric_value": 0.375, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 4, "metric_value": 0.375, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 4, "metric_value": 0.375, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[9]<=0.0:
											return 'viio/V'
										else: return 'viio/V'
									else: return 'viio/V'
								else: return 'viio/V'
							else: return 'viio/V'
						else: return 'viio/V'
					else: return 'viio/V'
				else: return 'viio/V'
			else: return 'viio/V'
		elif obj[2] == 'I':
			# {"feature": "t-2", "instances": 14, "metric_value": 0.5357, "depth": 3}
			if obj[1] == 'iv':
				# {"feature": "sadness", "instances": 8, "metric_value": 0.3667, "depth": 4}
				if obj[5]<=0.0:
					# {"feature": "love", "instances": 5, "metric_value": 0.2, "depth": 5}
					if obj[8]<=0.0:
						return 'V'
					elif obj[8]>0.0:
						# {"feature": "fear", "instances": 2, "metric_value": 0.0, "depth": 6}
						if obj[4]>0.0:
							return 'iv'
						elif obj[4]<=0.0:
							return 'V'
						else: return 'V'
					else: return 'iv'
				elif obj[5]>0.0:
					# {"feature": "joy", "instances": 3, "metric_value": 0.3333, "depth": 5}
					if obj[9]<=0.0:
						# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "fear", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0.0:
											return 'iv'
										else: return 'iv'
									else: return 'iv'
								else: return 'iv'
							else: return 'iv'
						else: return 'iv'
					elif obj[9]>0.0:
						return 'ii'
					else: return 'ii'
				else: return 'ii'
			elif obj[1] == 'V':
				# {"feature": "fear", "instances": 4, "metric_value": 0.25, "depth": 4}
				if obj[4]<=0.0:
					return 'V'
				elif obj[4]>0.0:
					# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						else: return 'i'
					else: return 'i'
				else: return 'i'
			elif obj[1] == 'iii':
				return 'bVII'
			elif obj[1] == 'vi':
				return 'V'
			else: return 'V'
		elif obj[2] == 'PAD':
			# {"feature": "sadness", "instances": 11, "metric_value": 0.5879, "depth": 3}
			if obj[5]<=0.49:
				# {"feature": "fear", "instances": 6, "metric_value": 0.2222, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "anger", "instances": 3, "metric_value": 0.3333, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "t-2", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[1] == 'START':
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'bVI'
										else: return 'bVI'
									else: return 'bVI'
								else: return 'bVI'
							else: return 'bVI'
						else: return 'bVI'
					elif obj[3]>0.0:
						return 'V'
					else: return 'V'
				elif obj[4]<=0.0:
					return 'iv'
				else: return 'iv'
			elif obj[5]>0.49:
				# {"feature": "t-2", "instances": 5, "metric_value": 0.56, "depth": 4}
				if obj[1] == 'START':
					# {"feature": "anger", "instances": 5, "metric_value": 0.56, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "fear", "instances": 5, "metric_value": 0.56, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "none", "instances": 5, "metric_value": 0.56, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 5, "metric_value": 0.56, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 5, "metric_value": 0.56, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 5, "metric_value": 0.56, "depth": 10}
										if obj[9]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						else: return 'V'
					else: return 'V'
				else: return 'V'
			else: return 'V'
		elif obj[2] == 'iv':
			# {"feature": "t-2", "instances": 8, "metric_value": 0.125, "depth": 3}
			if obj[1] == 'I':
				return 'V'
			elif obj[1] == 'V':
				# {"feature": "sadness", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[5]<=0.49:
					return 'i'
				elif obj[5]>0.49:
					return 'iv'
				else: return 'iv'
			elif obj[1] == 'IV':
				return 'I'
			elif obj[1] == 'ii':
				return 'viio/ii'
			elif obj[1] == 'viio/V':
				return 'bVI'
			else: return 'bVI'
		elif obj[2] == 'iii':
			# {"feature": "t-2", "instances": 5, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'bVI':
				return 'V'
			elif obj[1] == 'vii':
				return 'vii'
			elif obj[1] == 'V':
				return 'ii'
			else: return 'ii'
		elif obj[2] == 'viio/V':
			# {"feature": "anger", "instances": 4, "metric_value": 0.25, "depth": 3}
			if obj[3]<=0.11:
				# {"feature": "fear", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[4]<=0.0:
					return 'viio/ii'
				elif obj[4]>0.0:
					return 'V'
				else: return 'V'
			elif obj[3]>0.11:
				return 'ii'
			else: return 'ii'
		elif obj[2] == 'vi':
			# {"feature": "fear", "instances": 4, "metric_value": 0.0, "depth": 3}
			if obj[4]<=0.07:
				return 'V'
			elif obj[4]>0.07:
				return 'ii'
			else: return 'ii'
		elif obj[2] == 'bVI':
			return 'V'
		elif obj[2] == 'v':
			# {"feature": "t-2", "instances": 3, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'V':
				return 'ii'
			elif obj[1] == 'vii':
				return 'I'
			else: return 'I'
		elif obj[2] == 'bVII':
			return 'V'
		elif obj[2] == 'viio/ii':
			return 'V'
		elif obj[2] == 'START':
			return 'V'
		elif obj[2] == 'bIII':
			# {"feature": "t-2", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'iv':
				return 'viio/ii'
			elif obj[1] == 'bVI':
				return 'V'
			else: return 'V'
		elif obj[2] == 'IV':
			# {"feature": "t-2", "instances": 2, "metric_value": 0.5, "depth": 3}
			if obj[1] == 'I':
				# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "fear", "instances": 2, "metric_value": 0.5, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						else: return 'V'
					else: return 'V'
				else: return 'V'
			else: return 'V'
		elif obj[2] == 'bvii':
			return 'V'
		elif obj[2] == 'vii':
			# {"feature": "t-2", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'iii':
				return 'V'
			elif obj[1] == 'V':
				return 'bVII'
			else: return 'bVII'
		else: return 'V'
	elif obj[0] == 'ii':
		# {"feature": "t-2", "instances": 119, "metric_value": 0.4899, "depth": 2}
		if obj[1] == 'i':
			# {"feature": "t-3", "instances": 30, "metric_value": 0.3538, "depth": 3}
			if obj[2] == 'V':
				# {"feature": "sadness", "instances": 13, "metric_value": 0.6111, "depth": 4}
				if obj[5]<=0.0:
					# {"feature": "anger", "instances": 9, "metric_value": 0.6667, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "fear", "instances": 6, "metric_value": 0.6667, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "none", "instances": 6, "metric_value": 0.6667, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 6, "metric_value": 0.6667, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 6, "metric_value": 0.6667, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 6, "metric_value": 0.6667, "depth": 10}
										if obj[9]<=0.0:
											return 'v'
										else: return 'v'
									else: return 'v'
								else: return 'v'
							else: return 'v'
						else: return 'v'
					elif obj[3]>0.0:
						# {"feature": "fear", "instances": 3, "metric_value": 0.3333, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						elif obj[4]>0.0:
							return 'bIII'
						else: return 'bIII'
					else: return 'bIII'
				elif obj[5]>0.0:
					# {"feature": "fear", "instances": 4, "metric_value": 0.25, "depth": 5}
					if obj[4]>0.0:
						return 'V'
					elif obj[4]<=0.0:
						# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						else: return 'V'
					else: return 'V'
				else: return 'V'
			elif obj[2] == 'ii':
				# {"feature": "fear", "instances": 4, "metric_value": 0.3333, "depth": 4}
				if obj[4]<=0.0:
					# {"feature": "anger", "instances": 3, "metric_value": 0.4444, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "sadness", "instances": 3, "metric_value": 0.4444, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						else: return 'i'
					else: return 'i'
				elif obj[4]>0.0:
					return 'V'
				else: return 'V'
			elif obj[2] == 'iv':
				return 'V'
			elif obj[2] == 'viio/ii':
				return 'i'
			elif obj[2] == 'i':
				return 'V'
			elif obj[2] == 'I':
				return 'V'
			elif obj[2] == 'bIII':
				return 'V'
			elif obj[2] == 'START':
				return 'i'
			elif obj[2] == 'vii':
				return 'V'
			else: return 'V'
		elif obj[1] == 'vi':
			# {"feature": "t-3", "instances": 22, "metric_value": 0.3795, "depth": 3}
			if obj[2] == 'I':
				# {"feature": "love", "instances": 8, "metric_value": 0.2083, "depth": 4}
				if obj[8]>0.0:
					# {"feature": "anger", "instances": 6, "metric_value": 0.2778, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "fear", "instances": 6, "metric_value": 0.2778, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "sadness", "instances": 6, "metric_value": 0.2778, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 6, "metric_value": 0.2778, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 6, "metric_value": 0.2778, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 6, "metric_value": 0.2778, "depth": 10}
										if obj[9]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						else: return 'V'
					else: return 'V'
				elif obj[8]<=0.0:
					return 'V'
				else: return 'V'
			elif obj[2] == 'IV':
				# {"feature": "anger", "instances": 5, "metric_value": 0.32, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "fear", "instances": 5, "metric_value": 0.32, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 5, "metric_value": 0.32, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 5, "metric_value": 0.32, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 5, "metric_value": 0.32, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 5, "metric_value": 0.32, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "joy", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[9]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							else: return 'I'
						else: return 'I'
					else: return 'I'
				else: return 'I'
			elif obj[2] == 'ii':
				# {"feature": "fear", "instances": 4, "metric_value": 0.3333, "depth": 4}
				if obj[4]<=0.0:
					# {"feature": "anger", "instances": 3, "metric_value": 0.4444, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "sadness", "instances": 3, "metric_value": 0.4444, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=0.0:
											return 'IV'
										else: return 'IV'
									else: return 'IV'
								else: return 'IV'
							else: return 'IV'
						else: return 'IV'
					else: return 'IV'
				elif obj[4]>0.0:
					return 'v'
				else: return 'v'
			elif obj[2] == 'vi':
				# {"feature": "sadness", "instances": 4, "metric_value": 0.25, "depth": 4}
				if obj[5]>0.0:
					return 'V'
				elif obj[5]<=0.0:
					# {"feature": "love", "instances": 2, "metric_value": 0.0, "depth": 5}
					if obj[8]>0.5:
						return 'bIII'
					elif obj[8]<=0.5:
						return 'ii'
					else: return 'ii'
				else: return 'bIII'
			elif obj[2] == 'v':
				return 'v'
			else: return 'v'
		elif obj[1] == 'V':
			# {"feature": "t-3", "instances": 18, "metric_value": 0.0741, "depth": 3}
			if obj[2] == 'ii':
				return 'V'
			elif obj[2] == 'V':
				return 'V'
			elif obj[2] == 'I':
				# {"feature": "anger", "instances": 3, "metric_value": 0.4444, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "fear", "instances": 3, "metric_value": 0.4444, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 3, "metric_value": 0.4444, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						else: return 'V'
					else: return 'V'
				else: return 'V'
			elif obj[2] == 'IV':
				return 'V'
			elif obj[2] == 'iv':
				return 'V'
			elif obj[2] == 'viio/V':
				return 'vi'
			elif obj[2] == 'START':
				return 'V'
			else: return 'V'
		elif obj[1] == 'I':
			# {"feature": "t-3", "instances": 14, "metric_value": 0.3175, "depth": 3}
			if obj[2] == 'V':
				# {"feature": "love", "instances": 9, "metric_value": 0.4556, "depth": 4}
				if obj[8]<=0.0:
					# {"feature": "fear", "instances": 5, "metric_value": 0.3, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "anger", "instances": 4, "metric_value": 0.375, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "sadness", "instances": 4, "metric_value": 0.375, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 4, "metric_value": 0.375, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 4, "metric_value": 0.375, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[9]<=1.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						else: return 'V'
					elif obj[4]>0.0:
						return 'V'
					else: return 'V'
				elif obj[8]>0.0:
					# {"feature": "anger", "instances": 4, "metric_value": 0.625, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "fear", "instances": 4, "metric_value": 0.625, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "sadness", "instances": 4, "metric_value": 0.625, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 4, "metric_value": 0.625, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 4, "metric_value": 0.625, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 4, "metric_value": 0.625, "depth": 10}
										if obj[9]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						else: return 'V'
					else: return 'V'
				else: return 'V'
			elif obj[2] == 'IV':
				return 'V'
			elif obj[2] == 'START':
				return 'ii'
			else: return 'ii'
		elif obj[1] == 'ii':
			# {"feature": "t-3", "instances": 8, "metric_value": 0.1875, "depth": 3}
			if obj[2] == 'ii':
				# {"feature": "anger", "instances": 4, "metric_value": 0.375, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "fear", "instances": 4, "metric_value": 0.375, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 4, "metric_value": 0.375, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 4, "metric_value": 0.375, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 4, "metric_value": 0.375, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 4, "metric_value": 0.375, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[9]<=0.0:
											return 'ii'
										else: return 'ii'
									else: return 'ii'
								else: return 'ii'
							else: return 'ii'
						else: return 'ii'
					else: return 'ii'
				else: return 'ii'
			elif obj[2] == 'vi':
				return 'V'
			elif obj[2] == 'V':
				return 'i'
			elif obj[2] == 'I':
				return 'I'
			elif obj[2] == 'viio/ii':
				return 'ii'
			else: return 'ii'
		elif obj[1] == 'v':
			# {"feature": "t-3", "instances": 7, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'vi':
				return 'V'
			elif obj[2] == 'V':
				return 'vi'
			elif obj[2] == 'ii':
				return 'V'
			elif obj[2] == 'i':
				return 'v'
			elif obj[2] == 'viio/ii':
				return 'v'
			else: return 'v'
		elif obj[1] == 'viio/ii':
			# {"feature": "t-3", "instances": 5, "metric_value": 0.4667, "depth": 3}
			if obj[2] == 'bVI':
				# {"feature": "anger", "instances": 3, "metric_value": 0.3333, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "fear", "instances": 2, "metric_value": 0.5, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						else: return 'i'
					else: return 'i'
				elif obj[3]<=0.0:
					return 'i'
				else: return 'i'
			elif obj[2] == 'ii':
				# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "fear", "instances": 2, "metric_value": 0.5, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'ii'
										else: return 'ii'
									else: return 'ii'
								else: return 'ii'
							else: return 'ii'
						else: return 'ii'
					else: return 'ii'
				else: return 'ii'
			else: return 'ii'
		elif obj[1] == 'IV':
			# {"feature": "t-3", "instances": 4, "metric_value": 0.3333, "depth": 3}
			if obj[2] == 'I':
				# {"feature": "fear", "instances": 3, "metric_value": 0.0, "depth": 4}
				if obj[4]<=0.0:
					return 'V'
				elif obj[4]>0.0:
					return 'I'
				else: return 'I'
			elif obj[2] == 'iii':
				return 'vii'
			else: return 'vii'
		elif obj[1] == 'vii':
			# {"feature": "t-3", "instances": 3, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'V':
				return 'vii'
			elif obj[2] == 'ii':
				return 'V'
			else: return 'V'
		elif obj[1] == 'iii':
			return 'V'
		elif obj[1] == 'iv':
			return 'i'
		elif obj[1] == 'bVI':
			return 'V'
		elif obj[1] == 'bIII':
			return 'bIII'
		else: return 'bIII'
	elif obj[0] == 'IV':
		# {"feature": "t-2", "instances": 58, "metric_value": 0.5496, "depth": 2}
		if obj[1] == 'I':
			# {"feature": "t-3", "instances": 37, "metric_value": 0.518, "depth": 3}
			if obj[2] == 'V':
				# {"feature": "fear", "instances": 16, "metric_value": 0.3839, "depth": 4}
				if obj[4]<=0.0:
					# {"feature": "love", "instances": 14, "metric_value": 0.3469, "depth": 5}
					if obj[8]<=0.0:
						# {"feature": "anger", "instances": 7, "metric_value": 0.449, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "sadness", "instances": 7, "metric_value": 0.449, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 7, "metric_value": 0.449, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 7, "metric_value": 0.449, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 7, "metric_value": 0.449, "depth": 10}
										if obj[9]<=1.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							else: return 'I'
						else: return 'I'
					elif obj[8]>0.0:
						# {"feature": "sadness", "instances": 7, "metric_value": 0.2381, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "joy", "instances": 6, "metric_value": 0.2667, "depth": 7}
							if obj[9]<=0.0:
								# {"feature": "anger", "instances": 5, "metric_value": 0.32, "depth": 8}
								if obj[3]<=0.0:
									# {"feature": "none", "instances": 5, "metric_value": 0.32, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[7]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							elif obj[9]>0.0:
								return 'I'
							else: return 'I'
						elif obj[5]>0.0:
							return 'I'
						else: return 'I'
					else: return 'I'
				elif obj[4]>0.0:
					# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'bVI'
										else: return 'bVI'
									else: return 'bVI'
								else: return 'bVI'
							else: return 'bVI'
						else: return 'bVI'
					else: return 'bVI'
				else: return 'bVI'
			elif obj[2] == 'I':
				# {"feature": "love", "instances": 12, "metric_value": 0.5417, "depth": 4}
				if obj[8]>0.0:
					# {"feature": "anger", "instances": 8, "metric_value": 0.5, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "fear", "instances": 8, "metric_value": 0.5, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "sadness", "instances": 8, "metric_value": 0.5, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 8, "metric_value": 0.5, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 8, "metric_value": 0.5, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 8, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							else: return 'I'
						else: return 'I'
					else: return 'I'
				elif obj[8]<=0.0:
					# {"feature": "fear", "instances": 4, "metric_value": 0.3333, "depth": 5}
					if obj[4]<=0.5:
						# {"feature": "joy", "instances": 3, "metric_value": 0.3333, "depth": 6}
						if obj[9]>0.5:
							# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[3]<=0.0:
								# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[7]<=0.0:
											return 'ii'
										else: return 'ii'
									else: return 'ii'
								else: return 'ii'
							else: return 'ii'
						elif obj[9]<=0.5:
							return 'ii'
						else: return 'ii'
					elif obj[4]>0.5:
						return 'iv'
					else: return 'iv'
				else: return 'ii'
			elif obj[2] == 'IV':
				# {"feature": "love", "instances": 6, "metric_value": 0.4167, "depth": 4}
				if obj[8]<=0.57:
					# {"feature": "joy", "instances": 4, "metric_value": 0.3333, "depth": 5}
					if obj[9]>0.43:
						# {"feature": "anger", "instances": 3, "metric_value": 0.4444, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "fear", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "sadness", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[7]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							else: return 'I'
						else: return 'I'
					elif obj[9]<=0.43:
						return 'I'
					else: return 'I'
				elif obj[8]>0.57:
					# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "fear", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							else: return 'I'
						else: return 'I'
					else: return 'I'
				else: return 'I'
			elif obj[2] == 'i':
				return 'iv'
			elif obj[2] == 'iv':
				return 'I'
			else: return 'I'
		elif obj[1] == 'iv':
			# {"feature": "t-3", "instances": 5, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'I':
				return 'bvii'
			elif obj[2] == 'bVI':
				return 'bVII'
			elif obj[2] == 'iii':
				return 'i'
			else: return 'i'
		elif obj[1] == 'bVI':
			# {"feature": "love", "instances": 4, "metric_value": 0.3333, "depth": 3}
			if obj[8]<=0.18:
				# {"feature": "fear", "instances": 3, "metric_value": 0.3333, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "t-3", "instances": 2, "metric_value": 0.5, "depth": 5}
					if obj[2] == 'IV':
						# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'vi'
										else: return 'vi'
									else: return 'vi'
								else: return 'vi'
							else: return 'vi'
						else: return 'vi'
					else: return 'vi'
				elif obj[4]<=0.0:
					return 'bVI'
				else: return 'bVI'
			elif obj[8]>0.18:
				return 'vi'
			else: return 'vi'
		elif obj[1] == 'i':
			return 'bVII'
		elif obj[1] == 'iii':
			# {"feature": "t-3", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'I':
				return 'I'
			elif obj[2] == 'vi':
				return 'ii'
			else: return 'ii'
		elif obj[1] == 'bVII':
			return 'bVII'
		elif obj[1] == 'vi':
			# {"feature": "t-3", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'bVI':
				return 'V'
			elif obj[2] == 'iii':
				return 'I'
			else: return 'I'
		elif obj[1] == 'V':
			# {"feature": "t-3", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'viio/V':
				return 'V'
			elif obj[2] == 'I':
				return 'I'
			else: return 'I'
		elif obj[1] == 'ii':
			return 'iv'
		elif obj[1] == 'IV':
			return 'I'
		else: return 'I'
	elif obj[0] == 'bVI':
		# {"feature": "t-2", "instances": 58, "metric_value": 0.5454, "depth": 2}
		if obj[1] == 'V':
			# {"feature": "t-3", "instances": 18, "metric_value": 0.4568, "depth": 3}
			if obj[2] == 'bVI':
				# {"feature": "fear", "instances": 9, "metric_value": 0.5556, "depth": 4}
				if obj[4]<=0.0:
					# {"feature": "anger", "instances": 7, "metric_value": 0.5429, "depth": 5}
					if obj[3]>0.0:
						# {"feature": "sadness", "instances": 5, "metric_value": 0.5, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 4, "metric_value": 0.625, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 4, "metric_value": 0.625, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 4, "metric_value": 0.625, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 4, "metric_value": 0.625, "depth": 10}
										if obj[9]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						elif obj[5]>0.0:
							return 'V'
						else: return 'V'
					elif obj[3]<=0.0:
						# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'viio/ii'
										else: return 'viio/ii'
									else: return 'viio/ii'
								else: return 'viio/ii'
							else: return 'viio/ii'
						else: return 'viio/ii'
					else: return 'viio/ii'
				elif obj[4]>0.0:
					# {"feature": "love", "instances": 2, "metric_value": 0.0, "depth": 5}
					if obj[8]<=0.0:
						return 'iv'
					elif obj[8]>0.0:
						return 'ii'
					else: return 'ii'
				else: return 'iv'
			elif obj[2] == 'i':
				# {"feature": "anger", "instances": 3, "metric_value": 0.3333, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "fear", "instances": 2, "metric_value": 0.0, "depth": 5}
					if obj[4]<=0.0:
						return 'V'
					elif obj[4]>0.0:
						return 'vi'
					else: return 'vi'
				elif obj[3]>0.0:
					return 'i'
				else: return 'i'
			elif obj[2] == 'ii':
				return 'V'
			elif obj[2] == 'IV':
				return 'V'
			elif obj[2] == 'iv':
				return 'viio/ii'
			elif obj[2] == 'bVII':
				return 'viio/ii'
			elif obj[2] == 'viio/ii':
				return 'viio/ii'
			else: return 'viio/ii'
		elif obj[1] == 'viio/ii':
			# {"feature": "t-3", "instances": 8, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'bVI':
				return 'viio/ii'
			elif obj[2] == 'i':
				return 'V'
			elif obj[2] == 'iii':
				return 'viio/ii'
			else: return 'viio/ii'
		elif obj[1] == 'bIII':
			# {"feature": "t-3", "instances": 8, "metric_value": 0.3333, "depth": 3}
			if obj[2] == 'bVI':
				# {"feature": "love", "instances": 3, "metric_value": 0.0, "depth": 4}
				if obj[8]<=0.43:
					return 'I'
				elif obj[8]>0.43:
					return 'bVI'
				else: return 'bVI'
			elif obj[2] == 'i':
				# {"feature": "sadness", "instances": 3, "metric_value": 0.0, "depth": 4}
				if obj[5]>0.0:
					return 'bVII'
				elif obj[5]<=0.0:
					return 'iv'
				else: return 'iv'
			elif obj[2] == 'bVII':
				return 'i'
			elif obj[2] == 'viio/V':
				return 'I'
			else: return 'I'
		elif obj[1] == 'i':
			# {"feature": "love", "instances": 6, "metric_value": 0.4167, "depth": 3}
			if obj[8]<=0.0:
				# {"feature": "fear", "instances": 4, "metric_value": 0.3333, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "sadness", "instances": 3, "metric_value": 0.0, "depth": 5}
					if obj[5]<=0.0:
						return 'viio/V'
					elif obj[5]>0.0:
						return 'viio/ii'
					else: return 'viio/ii'
				elif obj[4]<=0.0:
					return 'V'
				else: return 'V'
			elif obj[8]>0.0:
				return 'bVI'
			else: return 'bVI'
		elif obj[1] == 'I':
			# {"feature": "fear", "instances": 5, "metric_value": 0.4, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "sadness", "instances": 3, "metric_value": 0.3333, "depth": 4}
				if obj[5]<=0.0:
					# {"feature": "love", "instances": 2, "metric_value": 0.0, "depth": 5}
					if obj[8]<=0.57:
						return 'bIII'
					elif obj[8]>0.57:
						return 'V'
					else: return 'V'
				elif obj[5]>0.0:
					return 'vi'
				else: return 'vi'
			elif obj[4]<=0.0:
				return 'vi'
			else: return 'vi'
		elif obj[1] == 'bVI':
			# {"feature": "t-3", "instances": 4, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'i':
				return 'iv'
			elif obj[2] == 'bIII':
				return 'I'
			else: return 'I'
		elif obj[1] == 'iii':
			# {"feature": "t-3", "instances": 3, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'I':
				return 'i'
			elif obj[2] == 'i':
				return 'viio/V'
			else: return 'viio/V'
		elif obj[1] == 'IV':
			return 'IV'
		elif obj[1] == 'viio/V':
			return 'V'
		elif obj[1] == 'bVII':
			return 'bIII'
		elif obj[1] == 'iv':
			return 'viio/ii'
		else: return 'viio/ii'
	elif obj[0] == 'vi':
		# {"feature": "t-2", "instances": 56, "metric_value": 0.5469, "depth": 2}
		if obj[1] == 'I':
			# {"feature": "t-3", "instances": 13, "metric_value": 0.4423, "depth": 3}
			if obj[2] == 'V':
				# {"feature": "love", "instances": 8, "metric_value": 0.4, "depth": 4}
				if obj[8]<=0.0:
					# {"feature": "anger", "instances": 5, "metric_value": 0.2667, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "fear", "instances": 3, "metric_value": 0.0, "depth": 6}
						if obj[4]<=0.0:
							return 'vi'
						elif obj[4]>0.0:
							return 'iv'
						else: return 'iv'
					elif obj[3]>0.0:
						return 'V'
					else: return 'V'
				elif obj[8]>0.0:
					return 'ii'
				else: return 'ii'
			elif obj[2] == 'I':
				return 'ii'
			elif obj[2] == 'i':
				return 'ii'
			elif obj[2] == 'START':
				return 'iii'
			else: return 'iii'
		elif obj[1] == 'iii':
			# {"feature": "t-3", "instances": 10, "metric_value": 0.4133, "depth": 3}
			if obj[2] == 'V':
				# {"feature": "love", "instances": 5, "metric_value": 0.2, "depth": 4}
				if obj[8]>0.5:
					return 'I'
				elif obj[8]<=0.5:
					# {"feature": "sadness", "instances": 2, "metric_value": 0.0, "depth": 5}
					if obj[5]>0.0:
						return 'V'
					elif obj[5]<=0.0:
						return 'vi'
					else: return 'vi'
				else: return 'V'
			elif obj[2] == 'I':
				# {"feature": "anger", "instances": 3, "metric_value": 0.4444, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "fear", "instances": 3, "metric_value": 0.4444, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 3, "metric_value": 0.4444, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=0.0:
											return 'iii'
										else: return 'iii'
									else: return 'iii'
								else: return 'iii'
							else: return 'iii'
						else: return 'iii'
					else: return 'iii'
				else: return 'iii'
			elif obj[2] == 'vii':
				return 'IV'
			elif obj[2] == 'vi':
				return 'vi'
			else: return 'vi'
		elif obj[1] == 'v':
			# {"feature": "t-3", "instances": 7, "metric_value": 0.1429, "depth": 3}
			if obj[2] == 'vi':
				# {"feature": "anger", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[3]>0.0:
					return 'v'
				elif obj[3]<=0.0:
					return 'vi'
				else: return 'vi'
			elif obj[2] == 'ii':
				return 'ii'
			elif obj[2] == 'I':
				return 'v'
			elif obj[2] == 'i':
				return 'v'
			else: return 'v'
		elif obj[1] == 'IV':
			# {"feature": "t-3", "instances": 6, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'I':
				return 'ii'
			elif obj[2] == 'bVI':
				return 'V'
			else: return 'V'
		elif obj[1] == 'V':
			# {"feature": "t-3", "instances": 5, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'iii':
				return 'I'
			elif obj[2] == 'IV':
				return 'V'
			elif obj[2] == 'I':
				return 'ii'
			elif obj[2] == 'ii':
				return 'bVII'
			else: return 'bVII'
		elif obj[1] == 'vi':
			return 'ii'
		elif obj[1] == 'bVI':
			# {"feature": "t-3", "instances": 4, "metric_value": 0.5, "depth": 3}
			if obj[2] == 'I':
				# {"feature": "fear", "instances": 3, "metric_value": 0.3333, "depth": 4}
				if obj[4]<=0.0:
					# {"feature": "love", "instances": 2, "metric_value": 0.0, "depth": 5}
					if obj[8]>0.0:
						return 'v'
					elif obj[8]<=0.0:
						return 'iii'
					else: return 'iii'
				elif obj[4]>0.0:
					return 'IV'
				else: return 'IV'
			elif obj[2] == 'V':
				return 'bVII'
			else: return 'bVII'
		elif obj[1] == 'ii':
			# {"feature": "t-3", "instances": 4, "metric_value": 0.25, "depth": 3}
			if obj[2] == 'V':
				# {"feature": "fear", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[4]<=0.0:
					return 'I'
				elif obj[4]>0.0:
					return 'ii'
				else: return 'ii'
			elif obj[2] == 'v':
				return 'ii'
			elif obj[2] == 'vi':
				return 'ii'
			else: return 'ii'
		elif obj[1] == 'bIII':
			return 'v'
		elif obj[1] == 'bVII':
			return 'bVII'
		else: return 'bVII'
	elif obj[0] == 'iv':
		# {"feature": "t-3", "instances": 55, "metric_value": 0.4994, "depth": 2}
		if obj[2] == 'i':
			# {"feature": "t-2", "instances": 15, "metric_value": 0.5444, "depth": 3}
			if obj[1] == 'I':
				# {"feature": "anger", "instances": 12, "metric_value": 0.5926, "depth": 4}
				if obj[3]<=0.39:
					# {"feature": "fear", "instances": 9, "metric_value": 0.5926, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 6, "metric_value": 0.6667, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "none", "instances": 6, "metric_value": 0.6667, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 6, "metric_value": 0.6667, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 6, "metric_value": 0.6667, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 6, "metric_value": 0.6667, "depth": 10}
										if obj[9]<=0.0:
											return 'ii'
										else: return 'ii'
									else: return 'ii'
								else: return 'ii'
							else: return 'ii'
						else: return 'ii'
					elif obj[4]>0.0:
						# {"feature": "sadness", "instances": 3, "metric_value": 0.3333, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						elif obj[5]>0.0:
							return 'V'
						else: return 'V'
					else: return 'V'
				elif obj[3]>0.39:
					# {"feature": "fear", "instances": 3, "metric_value": 0.3333, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						else: return 'i'
					elif obj[4]>0.0:
						return 'i'
					else: return 'i'
				else: return 'i'
			elif obj[1] == 'i':
				return 'i'
			elif obj[1] == 'V':
				return 'i'
			elif obj[1] == 'bIII':
				return 'bIII'
			else: return 'bIII'
		elif obj[2] == 'I':
			# {"feature": "t-2", "instances": 11, "metric_value": 0.1212, "depth": 3}
			if obj[1] == 'IV':
				return 'I'
			elif obj[1] == 'i':
				# {"feature": "anger", "instances": 3, "metric_value": 0.0, "depth": 4}
				if obj[3]>0.0:
					return 'i'
				elif obj[3]<=0.0:
					return 'bIII'
				else: return 'bIII'
			elif obj[1] == 'bvii':
				return 'i'
			elif obj[1] == 'I':
				return 'bVI'
			elif obj[1] == 'vi':
				return 'I'
			else: return 'I'
		elif obj[2] == 'V':
			# {"feature": "t-2", "instances": 9, "metric_value": 0.2222, "depth": 3}
			if obj[1] == 'i':
				return 'i'
			elif obj[1] == 'I':
				# {"feature": "sadness", "instances": 4, "metric_value": 0.3333, "depth": 4}
				if obj[5]>0.0:
					# {"feature": "anger", "instances": 3, "metric_value": 0.4444, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "fear", "instances": 3, "metric_value": 0.4444, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=0.0:
											return 'I'
										else: return 'I'
									else: return 'I'
								else: return 'I'
							else: return 'I'
						else: return 'I'
					else: return 'I'
				elif obj[5]<=0.0:
					return 'i'
				else: return 'i'
			elif obj[1] == 'bVI':
				return 'i'
			else: return 'i'
		elif obj[2] == 'bVI':
			# {"feature": "t-2", "instances": 4, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'bVI':
				return 'IV'
			elif obj[1] == 'I':
				return 'I'
			else: return 'I'
		elif obj[2] == 'iv':
			# {"feature": "t-2", "instances": 4, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'iii':
				return 'IV'
			elif obj[1] == 'i':
				return 'i'
			elif obj[1] == 'V':
				return 'bvii'
			elif obj[1] == 'I':
				return 'i'
			else: return 'i'
		elif obj[2] == 'START':
			# {"feature": "anger", "instances": 3, "metric_value": 0.3333, "depth": 3}
			if obj[3]<=0.0:
				# {"feature": "sadness", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[5]<=0.0:
					return 'viio/V'
				elif obj[5]>0.0:
					return 'V'
				else: return 'V'
			elif obj[3]>0.0:
				return 'i'
			else: return 'i'
		elif obj[2] == 'IV':
			return 'V'
		elif obj[2] == 'ii':
			return 'V'
		elif obj[2] == 'bIII':
			# {"feature": "t-2", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'bIII':
				return 'i'
			elif obj[1] == 'bVI':
				return 'I'
			else: return 'I'
		elif obj[2] == 'v':
			return 'V'
		elif obj[2] == 'iii':
			return 'V'
		else: return 'V'
	elif obj[0] == 'iii':
		# {"feature": "t-2", "instances": 47, "metric_value": 0.6375, "depth": 2}
		if obj[1] == 'I':
			# {"feature": "t-3", "instances": 16, "metric_value": 0.5972, "depth": 3}
			if obj[2] == 'V':
				# {"feature": "love", "instances": 9, "metric_value": 0.7037, "depth": 4}
				if obj[8]<=0.0:
					# {"feature": "anger", "instances": 6, "metric_value": 0.5333, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "sadness", "instances": 5, "metric_value": 0.5, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "fear", "instances": 4, "metric_value": 0.5, "depth": 7}
							if obj[4]>0.0:
								# {"feature": "none", "instances": 3, "metric_value": 0.6667, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 3, "metric_value": 0.6667, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.6667, "depth": 10}
										if obj[9]<=0.0:
											return 'bVI'
										else: return 'bVI'
									else: return 'bVI'
								else: return 'bVI'
							elif obj[4]<=0.0:
								return 'I'
							else: return 'I'
						elif obj[5]>0.0:
							return 'bVI'
						else: return 'bVI'
					elif obj[3]>0.0:
						return 'ii'
					else: return 'ii'
				elif obj[8]>0.0:
					# {"feature": "fear", "instances": 3, "metric_value": 0.3333, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "joy", "instances": 2, "metric_value": 0.0, "depth": 6}
						if obj[9]>0.0:
							return 'viio/ii'
						elif obj[9]<=0.0:
							return 'vi'
						else: return 'vi'
					elif obj[4]>0.0:
						return 'vii'
					else: return 'vii'
				else: return 'viio/ii'
			elif obj[2] == 'IV':
				# {"feature": "joy", "instances": 4, "metric_value": 0.0, "depth": 4}
				if obj[9]>0.0:
					return 'bVII'
				elif obj[9]<=0.0:
					return 'i'
				else: return 'i'
			elif obj[2] == 'I':
				return 'IV'
			elif obj[2] == 'ii':
				return 'vi'
			elif obj[2] == 'i':
				return 'ii'
			else: return 'ii'
		elif obj[1] == 'V':
			# {"feature": "fear", "instances": 9, "metric_value": 0.1852, "depth": 3}
			if obj[4]<=0.21:
				# {"feature": "love", "instances": 6, "metric_value": 0.2222, "depth": 4}
				if obj[8]<=0.51:
					return 'vi'
				elif obj[8]>0.51:
					# {"feature": "t-3", "instances": 3, "metric_value": 0.4444, "depth": 5}
					if obj[2] == 'I':
						# {"feature": "anger", "instances": 3, "metric_value": 0.4444, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "sadness", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=0.0:
											return 'vi'
										else: return 'vi'
									else: return 'vi'
								else: return 'vi'
							else: return 'vi'
						else: return 'vi'
					else: return 'vi'
				else: return 'vi'
			elif obj[4]>0.21:
				return 'V'
			else: return 'V'
		elif obj[1] == 'vi':
			# {"feature": "t-3", "instances": 5, "metric_value": 0.2, "depth": 3}
			if obj[2] == 'iii':
				# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "fear", "instances": 2, "metric_value": 0.5, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'vi'
										else: return 'vi'
									else: return 'vi'
								else: return 'vi'
							else: return 'vi'
						else: return 'vi'
					else: return 'vi'
				else: return 'vi'
			elif obj[2] == 'I':
				return 'ii'
			elif obj[2] == 'vii':
				return 'viio/ii'
			elif obj[2] == 'bVI':
				return 'IV'
			else: return 'IV'
		elif obj[1] == 'vii':
			# {"feature": "sadness", "instances": 5, "metric_value": 0.5, "depth": 3}
			if obj[5]<=0.0:
				# {"feature": "fear", "instances": 4, "metric_value": 0.5, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "t-3", "instances": 3, "metric_value": 0.3333, "depth": 5}
					if obj[2] == 'iii':
						# {"feature": "anger", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[3]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						else: return 'V'
					elif obj[2] == 'ii':
						return 'iii'
					else: return 'iii'
				elif obj[4]<=0.0:
					return 'V'
				else: return 'V'
			elif obj[5]>0.0:
				return 'i'
			else: return 'i'
		elif obj[1] == 'IV':
			return 'vii'
		elif obj[1] == 'bIII':
			# {"feature": "t-3", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'ii':
				return 'iv'
			elif obj[2] == 'I':
				return 'vii'
			else: return 'vii'
		elif obj[1] == 'i':
			# {"feature": "anger", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[3]<=0.0:
				return 'iii'
			elif obj[3]>0.0:
				return 'bVI'
			else: return 'bVI'
		elif obj[1] == 'iii':
			# {"feature": "t-3", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[2] == 'i':
				return 'iv'
			elif obj[2] == 'vii':
				return 'vii'
			else: return 'vii'
		elif obj[1] == 'bVI':
			return 'V'
		elif obj[1] == 'v':
			return 'vi'
		elif obj[1] == 'viio/V':
			return 'vii'
		elif obj[1] == 'iv':
			return 'iv'
		else: return 'iv'
	elif obj[0] == 'viio/ii':
		# {"feature": "t-3", "instances": 26, "metric_value": 0.5077, "depth": 2}
		if obj[2] == 'viio/ii':
			# {"feature": "sadness", "instances": 10, "metric_value": 0.3, "depth": 3}
			if obj[5]<=0.15:
				# {"feature": "anger", "instances": 8, "metric_value": 0.3, "depth": 4}
				if obj[3]>0.82:
					# {"feature": "t-2", "instances": 5, "metric_value": 0.2667, "depth": 5}
					if obj[1] == 'bVI':
						# {"feature": "fear", "instances": 3, "metric_value": 0.4444, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=0.0:
											return 'bVI'
										else: return 'bVI'
									else: return 'bVI'
								else: return 'bVI'
							else: return 'bVI'
						else: return 'bVI'
					elif obj[1] == 'ii':
						return 'ii'
					else: return 'ii'
				elif obj[3]<=0.82:
					return 'ii'
				else: return 'ii'
			elif obj[5]>0.15:
				return 'i'
			else: return 'i'
		elif obj[2] == 'V':
			# {"feature": "t-2", "instances": 5, "metric_value": 0.4, "depth": 3}
			if obj[1] == 'i':
				# {"feature": "fear", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[4]<=0.0:
					return 'V'
				elif obj[4]>0.0:
					return 'I'
				else: return 'I'
			elif obj[1] == 'bVI':
				# {"feature": "sadness", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[5]>0.0:
					return 'i'
				elif obj[5]<=0.0:
					return 'V'
				else: return 'V'
			elif obj[1] == 'I':
				return 'bVII'
			else: return 'bVII'
		elif obj[2] == 'ii':
			# {"feature": "fear", "instances": 4, "metric_value": 0.3333, "depth": 3}
			if obj[4]<=0.0:
				# {"feature": "t-2", "instances": 3, "metric_value": 0.4444, "depth": 4}
				if obj[1] == 'i':
					# {"feature": "anger", "instances": 3, "metric_value": 0.4444, "depth": 5}
					if obj[3]<=0.0:
						# {"feature": "sadness", "instances": 3, "metric_value": 0.4444, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=0.0:
											return 'i'
										else: return 'i'
									else: return 'i'
								else: return 'i'
							else: return 'i'
						else: return 'i'
					else: return 'i'
				else: return 'i'
			elif obj[4]>0.0:
				return 'bVI'
			else: return 'bVI'
		elif obj[2] == 'iv':
			# {"feature": "t-2", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'i':
				return 'i'
			elif obj[1] == 'bVI':
				return 'viio/ii'
			else: return 'viio/ii'
		elif obj[2] == 'i':
			# {"feature": "t-2", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'bVI':
				return 'bVI'
			elif obj[1] == 'v':
				return 'v'
			else: return 'v'
		elif obj[2] == 'vi':
			return 'V'
		elif obj[2] == 'bVI':
			return 'viio/V'
		elif obj[2] == 'I':
			return 'bVI'
		else: return 'bVI'
	elif obj[0] == 'bIII':
		# {"feature": "t-3", "instances": 26, "metric_value": 0.3205, "depth": 2}
		if obj[2] == 'bVI':
			# {"feature": "t-2", "instances": 4, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'viio/V':
				return 'bIII'
			elif obj[1] == 'bVII':
				return 'i'
			else: return 'i'
		elif obj[2] == 'bVII':
			# {"feature": "fear", "instances": 4, "metric_value": 0.0, "depth": 3}
			if obj[4]>0.0:
				return 'bVI'
			elif obj[4]<=0.0:
				return 'bVII'
			else: return 'bVII'
		elif obj[2] == 'bIII':
			# {"feature": "t-2", "instances": 4, "metric_value": 0.25, "depth": 3}
			if obj[1] == 'bVII':
				# {"feature": "fear", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[4]>0.0:
					return 'i'
				elif obj[4]<=0.0:
					return 'V'
				else: return 'V'
			elif obj[1] == 'ii':
				return 'iii'
			elif obj[1] == 'iv':
				return 'V'
			else: return 'V'
		elif obj[2] == 'V':
			# {"feature": "fear", "instances": 3, "metric_value": 0.0, "depth": 3}
			if obj[4]<=0.0:
				return 'V'
			elif obj[4]>0.0:
				return 'bVI'
			else: return 'bVI'
		elif obj[2] == 'iii':
			return 'I'
		elif obj[2] == 'i':
			return 'V'
		elif obj[2] == 'viio/V':
			# {"feature": "anger", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[3]>0.0:
				return 'iv'
			elif obj[3]<=0.0:
				return 'i'
			else: return 'i'
		elif obj[2] == 'iv':
			return 'iv'
		elif obj[2] == 'I':
			return 'bVI'
		elif obj[2] == 'ii':
			return 'bVI'
		elif obj[2] == 'vi':
			return 'i'
		elif obj[2] == 'viio/ii':
			return 'bVI'
		else: return 'bVI'
	elif obj[0] == 'bVII':
		# {"feature": "t-3", "instances": 25, "metric_value": 0.3707, "depth": 2}
		if obj[2] == 'bVII':
			# {"feature": "t-2", "instances": 6, "metric_value": 0.2222, "depth": 3}
			if obj[1] == 'IV':
				# {"feature": "joy", "instances": 3, "metric_value": 0.0, "depth": 4}
				if obj[9]<=0.2:
					return 'V'
				elif obj[9]>0.2:
					return 'vii'
				else: return 'vii'
			elif obj[1] == 'bIII':
				return 'bIII'
			elif obj[1] == 'vi':
				return 'bVII'
			else: return 'bVII'
		elif obj[2] == 'V':
			# {"feature": "fear", "instances": 5, "metric_value": 0.4667, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "t-2", "instances": 3, "metric_value": 0.0, "depth": 4}
				if obj[1] == 'i':
					return 'bVI'
				elif obj[1] == 'vi':
					return 'vi'
				else: return 'vi'
			elif obj[4]<=0.0:
				# {"feature": "anger", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[3]>0.0:
					return 'ii'
				elif obj[3]<=0.0:
					return 'bIII'
				else: return 'bIII'
			else: return 'ii'
		elif obj[2] == 'IV':
			return 'bIII'
		elif obj[2] == 'I':
			# {"feature": "t-2", "instances": 3, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'iii':
				return 'ii'
			elif obj[1] == 'viio/ii':
				return 'IV'
			else: return 'IV'
		elif obj[2] == 'iv':
			return 'bVII'
		elif obj[2] == 'i':
			return 'v'
		elif obj[2] == 'bIII':
			return 'bIII'
		elif obj[2] == 'vi':
			return 'IV'
		elif obj[2] == 'bVI':
			return 'IV'
		else: return 'IV'
	elif obj[0] == 'vii':
		# {"feature": "t-3", "instances": 23, "metric_value": 0.3826, "depth": 2}
		if obj[2] == 'V':
			# {"feature": "t-2", "instances": 5, "metric_value": 0.2, "depth": 3}
			if obj[1] == 'i':
				return 'i'
			elif obj[1] == 'I':
				# {"feature": "anger", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[3]<=0.0:
					return 'viio/V'
				elif obj[3]>0.0:
					return 'I'
				else: return 'I'
			elif obj[1] == 'iii':
				return 'bIII'
			else: return 'bIII'
		elif obj[2] == 'vii':
			# {"feature": "t-2", "instances": 5, "metric_value": 0.2667, "depth": 3}
			if obj[1] == 'i':
				# {"feature": "anger", "instances": 3, "metric_value": 0.0, "depth": 4}
				if obj[3]<=0.0:
					return 'V'
				elif obj[3]>0.0:
					return 'i'
				else: return 'i'
			elif obj[1] == 'ii':
				return 'ii'
			else: return 'ii'
		elif obj[2] == 'IV':
			# {"feature": "t-2", "instances": 3, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'ii':
				return 'iii'
			elif obj[1] == 'iii':
				return 'i'
			elif obj[1] == 'bVII':
				return 'vi'
			else: return 'vi'
		elif obj[2] == 'iv':
			return 'ii'
		elif obj[2] == 'bVII':
			return 'iii'
		elif obj[2] == 'viio/V':
			return 'iii'
		elif obj[2] == 'I':
			return 'bIII'
		elif obj[2] == 'bIII':
			return 'iii'
		elif obj[2] == 'iii':
			return 'iii'
		elif obj[2] == 'ii':
			return 'i'
		elif obj[2] == 'i':
			return 'i'
		else: return 'i'
	elif obj[0] == 'v':
		# {"feature": "t-3", "instances": 20, "metric_value": 0.4964, "depth": 2}
		if obj[2] == 'v':
			# {"feature": "t-2", "instances": 7, "metric_value": 0.6, "depth": 3}
			if obj[1] == 'vi':
				# {"feature": "anger", "instances": 5, "metric_value": 0.6, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "fear", "instances": 3, "metric_value": 0.6667, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "sadness", "instances": 3, "metric_value": 0.6667, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 3, "metric_value": 0.6667, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 3, "metric_value": 0.6667, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 3, "metric_value": 0.6667, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.6667, "depth": 10}
										if obj[9]<=0.0:
											return 'vi'
										else: return 'vi'
									else: return 'vi'
								else: return 'vi'
							else: return 'vi'
						else: return 'vi'
					else: return 'vi'
				elif obj[3]<=0.0:
					# {"feature": "fear", "instances": 2, "metric_value": 0.5, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "sadness", "instances": 2, "metric_value": 0.5, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 2, "metric_value": 0.5, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											return 'vi'
										else: return 'vi'
									else: return 'vi'
								else: return 'vi'
							else: return 'vi'
						else: return 'vi'
					else: return 'vi'
				else: return 'vi'
			elif obj[1] == 'ii':
				# {"feature": "fear", "instances": 2, "metric_value": 0.0, "depth": 4}
				if obj[4]<=0.0:
					return 'V'
				elif obj[4]>0.0:
					return 'bIII'
				else: return 'bIII'
			else: return 'V'
		elif obj[2] == 'i':
			# {"feature": "t-2", "instances": 4, "metric_value": 0.3333, "depth": 3}
			if obj[1] == 'ii':
				# {"feature": "anger", "instances": 3, "metric_value": 0.4444, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "fear", "instances": 3, "metric_value": 0.4444, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "sadness", "instances": 3, "metric_value": 0.4444, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 3, "metric_value": 0.4444, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=0.0:
											return 'V'
										else: return 'V'
									else: return 'V'
								else: return 'V'
							else: return 'V'
						else: return 'V'
					else: return 'V'
				else: return 'V'
			elif obj[1] == 'V':
				return 'i'
			else: return 'i'
		elif obj[2] == 'vi':
			# {"feature": "t-2", "instances": 3, "metric_value": 0.6667, "depth": 3}
			if obj[1] == 'ii':
				# {"feature": "anger", "instances": 3, "metric_value": 0.6667, "depth": 4}
				if obj[3]<=0.0:
					# {"feature": "fear", "instances": 3, "metric_value": 0.6667, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "sadness", "instances": 3, "metric_value": 0.6667, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "none", "instances": 3, "metric_value": 0.6667, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "irony", "instances": 3, "metric_value": 0.6667, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "love", "instances": 3, "metric_value": 0.6667, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "joy", "instances": 3, "metric_value": 0.6667, "depth": 10}
										if obj[9]<=0.0:
											return 'vii'
										else: return 'vii'
									else: return 'vii'
								else: return 'vii'
							else: return 'vii'
						else: return 'vii'
					else: return 'vii'
				else: return 'vii'
			else: return 'vii'
		elif obj[2] == 'I':
			return 'ii'
		elif obj[2] == 'V':
