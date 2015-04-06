#
#    Copyright 2014-2015
#
#      STIC - Universidad de La Laguna (ULL) <gesinv@ull.edu.es>
#
#    This file is part of Modelado de Servicios TIC.
#
#    Modelado de Servicios TIC is free software: you can redistribute it and/or modify it under
#    the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Modelado de Servicios TIC is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with Modelado de Servicios TIC.  If not, see
#    <http://www.gnu.org/licenses/>.
#

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
