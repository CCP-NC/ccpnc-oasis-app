from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Column,
    Dashboard,
    FilterMenu,
    FilterMenus,
    FilterMenuSizeEnum,
    Filters,
    Layout,
    Menu,
    MenuItemHistogram,
    MenuItemTerms,
    RowActionNorth,
    RowActions,
    RowDetails,
    Rows,
    RowSelection,
    SearchQuantities,
    WidgetPeriodicTable,
)

app_entry_point = AppEntryPoint(
    name='NewApp',
    description='NMR app entry point configuration.',
    app=App(
        label='CCP-NC NMR APP',
        path='app',
        category='simulation',
        # Load search quantities from custom schema first
        search_quantities=SearchQuantities(
            include=[
                '*#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                '*#nomad_simulations.schema_packages.model_system.ModelSystem',
                '*#nomad_simulations.schema_packages.atoms_state.AtomsState',
                '*#nomad_simulations.schema_packages.general.Program',
            ]
        ),
        # Add filters to ensure only entries with custom schema are shown
        filters_locked={
            'section_defs.definition_qualified_name': [
                'nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation'
            ]
        },
        columns=[
            Column(
                quantity='data.ccpnc_metadata.material_properties.chemical_name#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                label='Chemical Name',
                selected=True,
            ),
            Column(
                quantity='data.ccpnc_metadata.ccpnc_record.immutable_id#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                label='Magres Immutable ID',
                selected=True,
            ),
            Column(
                quantity='upload_create_time',
                label='Upload Time',
                selected=True,
            ),
            Column(
                quantity='main_author.name',
                label='Main Author',
                selected=True,
            )
        ],
        menu=Menu(
            title='NMR Filters',
            size='sm',
            items=[
                # Material properties submenu
                Menu(
                    title='Material Properties',
                    size='md',
                    items=[
                        MenuItemTerms(
                            quantity='data.ccpnc_metadata.material_properties.chemical_name#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                            options=10,
                            width=12,
                        ),
                    ],
                ),
                Menu(
                    title='DFT Code',
                    size='md',
                    items=[
                        MenuItemTerms(
                            quantity='data.program.name#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                            options=10,
                            width=12,
                        ),
                        MenuItemTerms(
                            quantity='data.program.version#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                            options=10,
                            width=12,
                        ),
                    ],
                ),
                Menu(
                    title='Elements / Formula',
                    size='md',
                    items=[
                        MenuItemTerms(
                            quantity='data.model_system.chemical_formula.iupac#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                            title='Chemical Formula IUPAC',
                            show_input=True,
                            options=0,  # Don't show formula options
                            width=12,
                        ),
                        MenuItemTerms(
                            quantity='data.model_system.chemical_formula.hill#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                            title='Chemical Formula Hill',
                            show_input=True,
                            options=0,  # Don't show formula options
                            width=12,
                        ),
                        MenuItemHistogram(
                            x='results.material.n_elements',
                        ),

                    ],
                ),
                Menu(
                    title='Author/Origin/Dataset',
                    size='md',
                    items=[
                        MenuItemTerms(
                            quantity='main_author.name',
                            title='Author name',
                            show_input=True,
                            options=10,  # Don't show formula options
                            width=12,
                        ),
                        MenuItemTerms(
                            quantity='data.ccpnc_metadata.ccpnc_record.immutable_id#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                            title='Magres Immutable ID',
                            show_input=True,
                            options=0,  # Don't show formula options
                            width=12,
                        ),
                        MenuItemHistogram(
                            x='upload_create_time',
                            autorange=False,
                        ),
                        MenuItemTerms(
                            quantity='data.ccpnc_metadata.external_database_reference.external_database_name#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                            title='External Database',
                            options=5,  # Show top 5 database options
                            width=12,
                        ),
                        MenuItemTerms(
                            quantity='data.ccpnc_metadata.external_database_reference.external_database_reference_code#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                            title='Database Reference Code',
                            show_input=True,
                            options=0,
                            width=12,
                        ),
                        MenuItemTerms(
                            quantity='data.ccpnc_metadata.publication_record.doi#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                            title='Publication DOI',
                            show_input=True,
                            options=0,
                            width=12,
                        ),
                        MenuItemTerms(
                            quantity='data.ccpnc_metadata.ccpnc_record.license#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                            title='License',
                            options=5,  # Show top 5 database options
                            width=12,
                        ),
                    ],
                ),
                Menu(
                    title='Functionals',
                    size='md',
                    items=[
                        MenuItemTerms(
                            quantity='results.method.simulation.dft.xc_functional_type',
                            title='Jacob\'s Ladder',
                            options=10,
                            width=12,
                        ),
                        MenuItemTerms(
                            quantity='results.method.simulation.dft.xc_functional_names',
                            title='XC Functional Names',
                            options=10,
                            width=12,
                        ),
                    ],
                ),
                Menu(
                    title='NMR Parameters',
                    size='md',
                    items=[
                        Menu(
                            title='Magnetic Shielding',
                            size='md',
                            items=[
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_magnetic_shielding.H_isotropy_list.isotropy#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Hydrogen (H)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_magnetic_shielding.C_isotropy_list.isotropy#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Carbon (C)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_magnetic_shielding.N_isotropy_list.isotropy#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Nitrogen (N)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_magnetic_shielding.F_isotropy_list.isotropy#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Fluorine (F)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_magnetic_shielding.Na_isotropy_list.isotropy#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Sodium (Na)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_magnetic_shielding.Al_isotropy_list.isotropy#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Aluminium (Al)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_magnetic_shielding.P_isotropy_list.isotropy#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Phosphorus (P)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_magnetic_shielding.Si_isotropy_list.isotropy#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Silicon (Si)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_magnetic_shielding.Cl_isotropy_list.isotropy#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Chlorine (Cl)',
                                    autorange=True,
                                    width=12,
                                ),
                            ]
                        ),
                        Menu(
                            title='Electric Field Gradient',
                            size='md',
                            items=[
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_electric_field_gradient.H_vzz_list.Vzz#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Hydrogen (H)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_electric_field_gradient.C_vzz_list.Vzz#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Carbon (C)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_electric_field_gradient.N_vzz_list.Vzz#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Nitrogen (N)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_electric_field_gradient.F_vzz_list.Vzz#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Fluorine (F)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_electric_field_gradient.Na_vzz_list.Vzz#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Sodium (Na)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_electric_field_gradient.Al_vzz_list.Vzz#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Aluminium (Al)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_electric_field_gradient.P_vzz_list.Vzz#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Phosphorus (P)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_electric_field_gradient.Si_vzz_list.Vzz#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Silicon (Si)',
                                    autorange=True,
                                    width=12,
                                ),
                                MenuItemHistogram(
                                    x='data.element_resolved_nmr_search.element_resolved_electric_field_gradient.Cl_vzz_list.Vzz#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                                    title='Chlorine (Cl)',
                                    autorange=True,
                                    width=12,
                                ),
                            ]
                        ),
                    ]
                ),
            ],
        ),
        dashboard=Dashboard(
            widgets=[
                WidgetPeriodicTable(
                    title = 'Elements of the material',
                    layout={
                        'lg': Layout(h=8, minH=8, minW=12, w=12, x=0, y=0),
                    },
                    search_quantity='results.material.elements',
                    scale='linear',
                )
            ]
        ),
    )
)

schema_name = (
    'nomad_oasis_schema_parser_plugin.schema_packages.schema_package.'
    'CCPNC_VoilaNotebook'
)
ccpnc_voila_app = AppEntryPoint(
    name='CCPNC Voila Notebook',
    description='CCPNC Voila Notebook app entry point configuration.',
    app=App(
        label = 'CCPNC Voila Notebook',
        path = 'upload-metadata',
        category = 'Tools',
        description = 'Download CCPNC metadata spreadsheet',
        filters=Filters(
            include=[
                f'*#{schema_name}'
            ]
        ),
        filters_locked={
            'section_defs.definition_qualified_name': schema_name
        },
        filter_menus=FilterMenus(
            options={
                'custom_quantities': FilterMenu(
                    label='Notebooks',
                    size=FilterMenuSizeEnum.L
                ),
                'author': FilterMenu(
                    label='Author',
                    size=FilterMenuSizeEnum.M
                ),
                'metadata': FilterMenu(
                    label='Visibility / IDs'
                ),
            }
        ),
        columns=[
            Column(
                quantity=f'data.name#{schema_name}',
                selected=True,
                label='Tool Name'
            ),
            Column(
                quantity=f'data.notebook_file#{schema_name}',
                label='Notebook File'
            ),
            Column(
                quantity='upload_create_time',
                label='Created',
                selected=True
            ),
        ],
        rows=Rows(
            actions=RowActions(
                options={
                    'launch': RowActionNorth(
                        tool_name='voila',
                        filepath=f'data.notebook_file#{schema_name}',
                    )
                }
            ),
            details=RowDetails(),
            selection=RowSelection(),
        ),
    )
)
